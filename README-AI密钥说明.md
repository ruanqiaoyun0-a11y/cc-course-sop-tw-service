# 终极考核 AI 密钥安全说明（小米 MiMo）

本微课（台湾团队学员服务流程及话术）的「终极考核：首通电话话术 Role-play」中，
AI 家长角色对话与 AI 综合评分均调用**小米 MiMo**（OpenAI 兼容端点，模型 mimo-v2.5-pro）。
本文说明 MiMo 密钥的安全存储与调用方式。

## 一、密钥如何加载（三不原则）

- **不硬编码**：源码 `index.html` 中只含占位符 `__MIMO_API_KEY__`，绝无明文密钥。
- **不入仓库**：真实密钥只存放在本地 `.env` 文件中，已被 `.gitignore` 排除，禁止提交到 Git。
- **不打印输出**：构建脚本 `_build.js` 与页面代码的任何分支都不会把密钥输出到终端、日志或控制台。

加载链路：
```
.env / 环境变量 MIMO_API_KEY
   → node _build.js（hex 混淆注入）
   → index.html 中 _HEX2 = '<hex>'
   → 页面 _rK2() 解码 → fetch(MIMO_API_URL) → Authorization: Bearer
```

## 二、构建与部署

```bash
# 首次：准备密钥
cp .env.example .env        # 编辑 .env 填入真实密钥（sk- 开头）

# 修改课程内容（章节/测验/话术）后重新生成台湾版数据
python _build.py            # 从 _content_*.py 重建课程数据与本地化（需 Python 3）
python _build.py --check    # 校验：章节数/测验数/残留词检查

# 每次修改 index.html 源码后重新注入密钥
node _build.js              # 注入密钥，生成可部署版本
node _build.js --check      # 校验：无占位符残留、hex 可解码、无明文密钥

# 部署 index.html（静态托管即可，无需服务器）
```

## 三、安全边界（务必知悉）

- 前端 hex 混淆**仅增加提取难度，并非加密**：任何有浏览器的访问者理论上都能
  从页面源码中还原密钥。纯静态部署下密钥最终必然出现在客户端。
- 适用场景：内部培训、访问受限的环境；如对安全要求高，请改用**服务端代理**
  （由后端持有密钥转发请求，前端只存代理地址）。
- MiMo 端点如未放行浏览器跨域（CORS），直连会被浏览器拦截，需自建同源代理转发。

## 四、调用要点

- 端点：`https://api.xiaomimimo.com/v1/chat/completions`
- 模型：`mimo-v2.5-pro`
- 认证：`Authorization: Bearer <key>`
- 评分使用 `response_format: { type: 'json_object' }` 结构化输出（如 MiMo 支持）；
  解析失败时自动降级为基础分，学员体验不中断。
- 学员侧限流：每小时 50 次 AI 调用（`STUDENT_LIMIT_PER_HOUR`）。
