#!/usr/bin/env node
/**
 * _build.js — 小米 MiMo API Key 安全注入构建脚本（零依赖）
 *
 * 用途：把密钥从环境变量 / .env 读取，以 hex 混淆形式注入 index.html 的
 *       _HEX2 占位符，生成可直接部署使用的最终版本。全程不打印密钥。
 *
 * 用法：
 *   node _build.js            构建（读取 MIMO_API_KEY 环境变量或同目录 .env）
 *   node _build.js --check    校验模式：断言已注入且无明文密钥残留
 *
 * 安全说明：
 *   - 密钥只从环境变量或 .env 读取，不写入任何源码/仓库文件
 *   - .env 已被 .gitignore 排除，禁止提交到仓库
 *   - 脚本任何分支都不会把密钥打印到终端/日志
 *   - 前端 hex 混淆仅增加提取难度，并非加密（详见 README）
 */
'use strict';

const fs = require('fs');
const path = require('path');

const DIR = __dirname;
const TARGET = path.join(DIR, 'index.html');
const PLACEHOLDER = '__MIMO_API_KEY__';
const PLACEHOLDER_HEX = Buffer.from(PLACEHOLDER, 'utf8').toString('hex');
const KEY_PREFIX = 'sk-';

function readDotEnv() {
  const envPath = path.join(DIR, '.env');
  if (!fs.existsSync(envPath)) return {};
  const out = {};
  for (const line of fs.readFileSync(envPath, 'utf8').split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const eq = trimmed.indexOf('=');
    if (eq <= 0) continue;
    const k = trimmed.slice(0, eq).trim();
    let v = trimmed.slice(eq + 1).trim();
    if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) {
      v = v.slice(1, -1);
    }
    out[k] = v;
  }
  return out;
}

function getKey() {
  const fromEnv = process.env.MIMO_API_KEY;
  if (fromEnv) return fromEnv;
  const fromFile = readDotEnv().MIMO_API_KEY;
  return fromFile || '';
}

function hexOf(str) {
  return Buffer.from(str, 'utf8').toString('hex');
}

function unhex(hex) {
  if (typeof hex !== 'string' || hex.length % 2 !== 0) return '';
  let o = '';
  for (let i = 0; i < hex.length; i += 2) o += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
  return o;
}

function normalizeTemplate(html) {
  // 幂等：若之前已注入（_HEX2 = '<hex>'），先还原为占位符，保证可重复构建
  const re = new RegExp("const _HEX2 = '[0-9a-fA-F]+';");
  if (re.test(html)) {
    html = html.replace(re, "const _HEX2 = '" + PLACEHOLDER + "';");
  }
  return html;
}

function build() {
  const key = getKey();
  if (!key) {
    console.error('[build] 错误：未找到 MIMO_API_KEY。请设置环境变量或在同目录 .env 中配置（见 .env.example）。');
    process.exit(1);
  }
  if (!key.startsWith(KEY_PREFIX)) {
    console.error('[build] 错误：MIMO_API_KEY 格式不正确（应以 sk- 开头）。');
    process.exit(1);
  }
  let html = fs.readFileSync(TARGET, 'utf8');
  html = normalizeTemplate(html);
  const placeholderDecl = "const _HEX2 = '" + PLACEHOLDER + "';";
  if (!html.includes(placeholderDecl)) {
    console.error('[build] 错误：index.html 中未找到 _HEX2 占位符声明，请确认模板未损坏。');
    process.exit(1);
  }
  html = html.replace(placeholderDecl, "const _HEX2 = '" + hexOf(key) + "';");
  fs.writeFileSync(TARGET, html, 'utf8');
  console.log('[build] 完成：密钥已注入（hex 混淆），index.html 可直接部署。');
}

function check() {
  const html = fs.readFileSync(TARGET, 'utf8');
  const problems = [];
  const m = html.match(/const _HEX2 = '([^']*)';/);
  if (!m) problems.push('未找到 _HEX2 声明');
  else if (m[1] === PLACEHOLDER || m[1].indexOf('__') === 0) problems.push('占位符未注入（仍是 __MIMO_API_KEY__）');
  else {
    const decoded = unhex(m[1]);
    if (!decoded.startsWith(KEY_PREFIX)) problems.push('hex 解码后不是 sk- 前缀（注入内容异常）');
  }
  // 全文不应出现明文密钥（长度 ≥ 16 的 sk- 串）
  const plain = html.match(/sk-[A-Za-z0-9]{16,}/);
  if (plain) problems.push('检测到明文密钥残留');
  if (problems.length) {
    console.error('[check] 未通过：');
    problems.forEach(p => console.error('  - ' + p));
    process.exit(1);
  }
  console.log('[check] 通过：占位符已注入、hex 可解码、无明文密钥残留。');
}

const mode = process.argv[2];
if (mode === '--check') check();
else if (mode === undefined || mode === '--build') build();
else {
  console.error('用法：node _build.js [--check | --build]');
  process.exit(1);
}
