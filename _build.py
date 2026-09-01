# -*- coding: utf-8 -*-
"""
_build.py — 台湾版班导服务微课 构建脚本（零依赖）
将已下载的参考站 index.html（港澳版）机械替换为台湾版：
  1) 数据层：courseData（8节）/ quizzes / roleplayConfig
  2) 状态与逻辑层：扩展为 7 章 + 终极考核
  3) AI 引擎：DeepSeek 直连 → 小米 MiMo（OpenAI 兼容协议，_HEX2/_rK2 占位）
  4) 本地化：微信→LINE、删除群表述、粤语→简体普通话、繁体→简体
用法：
  python _build.py           执行替换并写回 index.html
  python _build.py --check   校验（章节数/测验数/残留词检查）
"""
import json
import re
import sys

from _content_s12 import SECTIONS_S12
from _content_s34 import SECTIONS_S34
from _content_s56 import SECTIONS_S56
from _content_s78 import SECTIONS_S78
from _content_quizzes1 import QUIZZES_1
from _content_quizzes2 import QUIZZES_2
from _content_roleplay import ROLEPLAY

TARGET = 'index.html'
COURSE_TITLE = '台湾团队学员服务流程及话术'
LS_PREFIX = 'vipthink_tw_service'
SECTIONS = SECTIONS_S12 + SECTIONS_S34 + SECTIONS_S56 + SECTIONS_S78
QUIZZES = {**QUIZZES_1, **QUIZZES_2}


# ---------------------------------------------------------------
# JS 生成器
# ---------------------------------------------------------------
def js_str(s):
    """Python 字符串 → JS 单引号字符串（转义反斜杠/单引号/换行）"""
    return "'" + s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n') + "'"


def build_course_data_js():
    """生成 courseData 对象 JS（content 用模板字符串）"""
    lines = ['const courseData = {', "  title: " + js_str(COURSE_TITLE) + ',', '  sections: [']
    for sec in SECTIONS:
        lines.append('    {')
        lines.append('      id: ' + js_str(sec['id']) + ',')
        lines.append('      title: ' + js_str(sec['title']) + ',')
        lines.append('      duration: ' + js_str(sec['duration']) + ',')
        lines.append('      icon: ' + js_str(sec['icon']) + ',')
        lines.append('      type: ' + js_str(sec['type']) + ',')
        lines.append('      content: `' + sec['content'] + '`')
        lines.append('    },')
    lines.append('  ]')
    lines.append('};')
    return '\n'.join(lines)


def build_quizzes_js():
    return 'const quizzes = ' + json.dumps(QUIZZES, ensure_ascii=False, indent=2) + ';'


def build_roleplay_js():
    return 'const roleplayConfig = ' + json.dumps(ROLEPLAY, ensure_ascii=False, indent=2) + ';'


# ---------------------------------------------------------------
# 逻辑层块替换（7 章扩展 + MiMo 引擎）
# ---------------------------------------------------------------
STATE_VARS_JS = '''// 选择题状态 — 用 var 使其成为 window 的属性，保证 window['quiz1Answered'] 等动态访问正确
var quiz1Answered = false, quiz2Answered = false, quiz3Answered = false, quiz4Answered = false, quiz5Answered = false, quiz6Answered = false, quiz7Answered = false;
// AI对话状态 — 同理必须用 var
var dialogue1Answered = false, dialogue1Score = 0;
var dialogue2Answered = false, dialogue2Score = 0;
var dialogue3Answered = false, dialogue3Score = 0;
var dialogue4Answered = false, dialogue4Score = 0;
var dialogue5Answered = false, dialogue5Score = 0;
var dialogue6Answered = false, dialogue6Score = 0;
var dialogue7Answered = false, dialogue7Score = 0;
// 终极考核状态（自由对话模式）
var roleplaySubmitted = false, roleplayScore = 0;
let roleplayExchangeCount = 0;        // 当前对话轮数
let roleplayConversation = [];         // 完整对话记录 [{role:'user'|'parent', content:''}]'''

AI_CONFIG_JS = '''// ============================================================
// AI API 设置（公司统一直连小米 MiMo — 学员无需配置任何东西）
// 说明：MiMo API 支持 OpenAI 兼容协议与 CORS 跨域调用，前端可直接访问，
//       部署到任意静态托管（CloudStudio/Vercel/GitHub Pages）均可用。
//       Key 由构建脚本 _build.js 从 .env 读取，以 hex 混淆注入，运行时还原。
// ============================================================
const _HEX2 = '__MIMO_API_KEY__';
function _rK2(){if(!_HEX2||_HEX2.indexOf('__')===0)return '';let o='';for(let i=0;i<_HEX2.length;i+=2)o+=String.fromCharCode(parseInt(_HEX2.substr(i,2),16));return o;}
const MIMO_API_URL = 'https://api.xiaomimimo.com/v1/chat/completions';
const MIMO_MODEL = 'mimo-v2.5-pro';'''

CAN_NAVIGATE_JS = '''function canNavigateTo(index) {
  if (index <= 0) return { ok: true };
  for (let i = 1; i <= index && i <= 7; i++) {
    if (!window['quiz' + i + 'Answered'] || !window['dialogue' + i + 'Answered'] || window['dialogue' + i + 'Score'] < 60) {
      return { ok: false, msg: '请先完成第' + i + '章的选择题和AI模拟对话（对话需达60分）' };
    }
  }
  return { ok: true };
}'''

SAVE_PROGRESS_JS = '''function saveProgress() {
  // 多题时的子题状态
  const subKeys = [];
  for (let i = 1; i <= 7; i++) {
    const quiz = quizzes['quiz' + i];
    if (quiz && Array.isArray(quiz.questions)) {
      quiz.questions.forEach((_, qi) => {
        subKeys.push(['quiz' + i + '_q' + qi + '_Answered', window['quiz' + i + '_q' + qi + '_Answered'] || false]);
      });
    }
  }
  const subState = {};
  subKeys.forEach(([k, v]) => { subState[k] = v; });

  const q = {};
  for (let i = 1; i <= 7; i++) {
    q['quiz' + i + 'Answered'] = window['quiz' + i + 'Answered'];
    q['dialogue' + i + 'Answered'] = window['dialogue' + i + 'Answered'];
    q['dialogue' + i + 'Score'] = window['dialogue' + i + 'Score'];
  }
  const state = {
    completedSections: [...completedSections],
    ...q,
    roleplaySubmitted, roleplayScore,
    subAnswers: subState,
    currentSection
  };
  localStorage.setItem(LS_PREFIX + '_progress', JSON.stringify(state));
}'''

LOAD_PROGRESS_FIELDS_JS = '''      for (let i = 1; i <= 7; i++) {
        window['quiz' + i + 'Answered'] = saved['quiz' + i + 'Answered'] || false;
        window['dialogue' + i + 'Answered'] = saved['dialogue' + i + 'Answered'] || false;
        window['dialogue' + i + 'Score'] = saved['dialogue' + i + 'Score'] || 0;
      }'''

CHECK_CERTIFICATE_JS = '''  let allDone = completedSections.size >= courseData.sections.length && roleplaySubmitted && roleplayScore >= 60;
  for (let i = 1; i <= 7; i++) {
    if (!window['quiz' + i + 'Answered'] || !window['dialogue' + i + 'Answered']) { allDone = false; }
  }'''

FREE_CHAT_PROMPT_JS = '''function buildFreeChatSystemPrompt() {
  return `你扮演小明（5岁，幼稚园中班）的妈妈，正在接听VIP THINK班主任老师的首通电话。

【你的身份】
- 普通家长，不是教育专家
- 使用简体中文（普通话），语气自然口语化，像真实的台湾妈妈
- 回答简短自然，1-3句话
- 友善但不过度热情，像接陌生电话的普通家长

【孩子背景】
- 小明，5岁，幼稚园中班
- 之前没上过数学思维课
- 会一点点数，加减法还不会
- 有点慢热，表达能力一般

【核心规则 — 最重要！】
⚠️ 你必须根据老师（user）刚说的具体内容来回应！
✅ 正确做法：
- 老师说了有用信息 → 确认收到 + 自然反应
- 老师说得太快或不清楚 → 追问"不好意思，可以再说一次吗？"
- 老师说的内容奇怪 → 表现困惑
❌ 绝对禁止：
- 不管说什么都背诵固定台词
- 跳到下一个话题（老师还没讲完就问APP/请假等）
- 假装听懂乱码内容
- 每次都回答相同的话

【话题推进指引】
作为真实家长，你会自然地跟随老师的引导。当老师介绍完一个主题并开始下一个时，你也自然地切换关注点。整体对话应覆盖：
开场→基本信息→数学基础→性格期望→课程确认→APP使用→上课规则→福利收尾`;
}'''

# 选择题「答错可重答」：答对才锁定并计入完成；答错仅提示、不暴露正确答案、可重新作答
QUIZ_RETRY_JS = '''function selectQuizOption(el, optionIndex, quizId, questionIndex) {
  const quiz = quizzes[quizId];
  const isMulti = Array.isArray(quiz.questions) && quiz.questions.length > 0;
  const qi = (isMulti && typeof questionIndex === 'number') ? questionIndex : 0;

  // 取出对应题目
  const question = isMulti ? quiz.questions[qi] : quiz;

  // 多题时，按子题索引判断是否已答；单题时沿用原有 stateVar
  let stateVar;
  if (isMulti) {
    stateVar = quizId + '_q' + qi + '_Answered';
    if (window[stateVar]) return;
  } else {
    stateVar = quizId + 'Answered';
    if (window[stateVar]) return;
  }

  const feedback = isMulti
    ? document.getElementById('feedback-' + quizId + '-' + qi)
    : document.getElementById('feedback-' + quizId);
  const card = document.getElementById('quiz-card-' + quizId);
  const optionsSelector = isMulti
    ? ('#options-' + quizId + '-' + qi + ' .quiz-option')
    : ('#quiz-card-' + quizId + ' .quiz-option');
  const allOptions = document.querySelectorAll(optionsSelector);

  if (optionIndex === question.correct) {
    // 答对：锁定本题，显示正确反馈，计入完成
    allOptions.forEach(opt => {
      opt.style.pointerEvents = 'none';
      opt.classList.remove('selected', 'wrong');
    });
    el.classList.add('selected', 'correct');
    card.classList.add('answered-correct');
    card.classList.remove('answered-wrong');
    feedback.className = 'quiz-feedback show correct';
    feedback.innerHTML = question.feedback_correct;

    window[stateVar] = true;

    // 多题时，更新主状态：所有子题都答完才算"已答"
    if (isMulti) {
      const allAnswered = quiz.questions.every((_, i) => window[quizId + '_q' + i + '_Answered']);
      if (allAnswered) {
        window[quizId + 'Answered'] = true;
      }
    } else {
      window[quizId + 'Answered'] = true;
    }
    showToast('回答正确 ✓', 'success');
  } else {
    // 答错：不锁定、不暴露正确答案，允许重新作答
    allOptions.forEach(opt => {
      opt.style.pointerEvents = '';
      opt.classList.remove('selected', 'correct', 'wrong');
    });
    el.classList.add('selected', 'wrong');
    feedback.className = 'quiz-feedback show wrong';
    feedback.innerHTML = '❌ 回答错误，请重新选择。';
    showToast('回答错误，请重新选择', 'warning');
  }

  saveProgress();
  updateSidebarLocks();
}'''


def apply_blocks(html):
    """数据层 + 逻辑层块替换（按锚点定位）。
    注意：re.sub 的替换值用 lambda，避免反斜杠转义序列被解析（如 \\n 变真实换行）。
    """
    # 1) courseData
    html = re.sub(
        r"const courseData = \{[^\x00]*?\n\};",
        lambda m: build_course_data_js(),
        html, count=1, flags=re.DOTALL)
    # 2) quizzes
    html = re.sub(
        r"const quizzes = \{[^\x00]*?\n\};",
        lambda m: build_quizzes_js(),
        html, count=1, flags=re.DOTALL)
    # 3) roleplayConfig
    html = re.sub(
        r"const roleplayConfig = \{[^\x00]*?\n\};",
        lambda m: build_roleplay_js(),
        html, count=1, flags=re.DOTALL)
    # 4) 状态变量
    html = re.sub(
        r"// 选择题状态[\s\S]*?let roleplayConversation = \[\];.*?// 完整对话记录 \[\{role:'user'\|'parent', content:''\}\]",
        lambda m: STATE_VARS_JS,
        html, count=1)
    # 5) AI 配置块
    html = re.sub(
        r"// AI API 设置[\s\S]*?const DEEPSEEK_MODEL = 'deepseek-chat';",
        lambda m: AI_CONFIG_JS,
        html, count=1)
    # 6) canNavigateTo
    html = re.sub(
        r"function canNavigateTo\(index\) \{[\s\S]*?\n\}",
        lambda m: CAN_NAVIGATE_JS,
        html, count=1)
    # 7) saveProgress
    html = re.sub(
        r"function saveProgress\(\) \{[\s\S]*?\n\}",
        lambda m: SAVE_PROGRESS_JS,
        html, count=1)
    # 8) loadProgress 字段恢复
    html = re.sub(
        r"      quiz1Answered = saved\.quiz1Answered \|\| false;[\s\S]*?      dialogue4Score = saved\.dialogue4Score \|\| 0;",
        lambda m: LOAD_PROGRESS_FIELDS_JS,
        html, count=1)
    # 9) checkCertificate 条件
    html = re.sub(
        r"  const allDone = completedSections\.size >= courseData\.sections\.length[\s\S]*?&& roleplaySubmitted && roleplayScore >= 60;",
        lambda m: CHECK_CERTIFICATE_JS,
        html, count=1)
    # 10) AI 家长人设
    html = re.sub(
        r"function buildFreeChatSystemPrompt\(\) \{[\s\S]*?\n\}",
        lambda m: FREE_CHAT_PROMPT_JS,
        html, count=1)
    # 11) 选择题「答错可重答」
    html = re.sub(
        r"function selectQuizOption\(el, optionIndex, quizId, questionIndex\) \{[\s\S]*?\n\}",
        lambda m: QUIZ_RETRY_JS,
        html, count=1)
    return html


# ---------------------------------------------------------------
# 本地化替换
# ---------------------------------------------------------------
GLOBAL_REPLACEMENTS = [
    # 课程名 / 品牌
    ('港澳团队学员服务流程及话术', COURSE_TITLE),
    ('港澳', '台湾'),
    ('豌豆益智', 'VIP THINK'),
    # localStorage 前缀
    ('vipthink_hkmacau_service', LS_PREFIX),
    # AI 引擎重命名（先长后短）
    ('callDeepSeek', 'callAI'),
    ('DEEPSEEK_API_URL', 'MIMO_API_URL'),
    ('DEEPSEEK_MODEL', 'MIMO_MODEL'),
    ('_rK()', '_rK2()'),
    ('DeepSeek', 'MiMo'),
    # 通讯工具：微信 → LINE
    ('微信', 'LINE'),
    # 特定长句（含粤语/知识范围硬编码）
    ('輸入你嘅說話...（Ctrl+Enter 發送）', '输入你要说的话...（Ctrl+Enter 发送）'),
    ('請輸入回應內容', '请输入回应内容'),
    ('請輸入說話內容', '请输入说话内容'),
    ('📌 第1章知識點檢測：覆蓋24小時首通、課包核對、上課規則、APP&服務號、福利介紹',
     '📌 本章知识点检测：根据本章所学内容作答'),
    ('請以家長身份，針對這段內容做出簡短自然的粵語回應。',
     '请以家长身份，针对这段内容做出简短自然的普通话回应。'),
    ('你是豌豆益智培訓機構的資深教學評審官', '你是VIP THINK培训机构的资深教学评审官'),
    # MiMo 调用修复：关闭 thinking + max_tokens 参数名映射（mimo-v2.5-pro 必需）
    ("async function callAI(body) {\n  const response = await fetch(MIMO_API_URL, {\n    method: 'POST',\n    headers: {\n      'Content-Type': 'application/json',\n      'Authorization': 'Bearer ' + _rK2()\n    },\n    body: JSON.stringify(body)\n  });",
     "async function callAI(body) {\n  // mimo-v2.5-pro 需关闭 thinking 才能自定义 temperature；max_tokens 参数名映射为 max_completion_tokens\n  const payload = { ...body, model: body.model || MIMO_MODEL, thinking: { type: 'disabled' }, max_completion_tokens: body.max_completion_tokens || body.max_tokens || 500 };\n  const response = await fetch(MIMO_API_URL, {\n    method: 'POST',\n    headers: {\n      'Content-Type': 'application/json',\n      'Authorization': 'Bearer ' + _rK2()\n    },\n    body: JSON.stringify(payload)\n  });"),
]

# 繁体 → 简体 字符映射（作用于替换后的全文）
CHAR_MAP = {
    '課': '课', '學': '学', '員': '员', '話': '话', '術': '术', '參': '参',
    '開': '开', '場': '场', '題': '题', '對': '对', '評': '评', '測': '测',
    '檢': '检', '維': '维', '達': '达', '蓋': '盖', '準': '准', '確': '确',
    '讀': '读', '設': '设', '團': '团', '隊': '队', '結': '结', '業': '业',
    '證': '证', '書': '书', '習': '习', '進': '进', '時': '时', '長': '长',
    '記': '记', '錄': '录', '頻': '频', '誤': '误', '隱': '隐', '傳': '传',
    '遞': '递', '論': '论', '練': '练', '價': '价', '審': '审', '資': '资',
    '監': '监', '顧': '顾', '問': '问', '訊': '讯', '讓': '让', '請': '请',
    '輸': '输', '內': '内', '後': '后', '裡': '里', '來': '来', '們': '们',
    '幫': '帮', '幾': '几', '覺': '觉', '變': '变', '歡': '欢', '該': '该',
    '說': '说', '認': '认', '識': '识', '點': '点', '數': '数', '圖': '图',
    '運': '运', '較': '较', '單': '单', '簡': '简', '複': '复', '預': '预',
    '環': '环', '閉': '闭', '歸': '归', '標': '标', '狀': '状', '況': '况',
    '鏈': '链', '暫': '暂', '異': '异', '議': '议', '處': '处', '續': '续',
    '費': '费', '規': '规', '則': '则', '詳': '详', '節': '节', '調': '调',
    '籤': '签', '觸': '触', '連': '连', '絡': '络', '間': '间', '聯': '联',
    '號': '号', '碼': '码', '覽': '览', '網': '网', '頁': '页', '軟': '软',
    '體': '体', '專': '专', '務': '务', '範': '范', '親': '亲', '優': '优',
    '饋': '馈', '筆': '笔', '綜': '综', '過': '过', '極': '极', '輪': '轮',
    '擊': '击', '擬': '拟', '發': '发', '領': '领', '滿': '满', '獲': '获',
    '補': '补', '充': '充', '關': '关', '當': '当', '程': '程', '取': '取',
    '秀': '秀', '語': '语', '總': '总', '並': '并', '於': '于', '為': '为',
    '與': '与', '個': '个', '這': '这', '那': '那', '麼': '么', '還': '还',
    '要': '要', '會': '会', '從': '从', '現': '现', '態': '态', '據': '据',
    '報': '报', '導': '导', '師': '师', '選': '选', '擇': '择', '項': '项',
    '對': '对', '錯': '错', '誤': '误', '訓': '训', '練': '练', '評': '评',
    '估': '估', '表': '表', '現': '现', '計': '计', '劃': '划', '職': '职',
    '責': '责', '務': '务', '資': '资', '訊': '讯', '聯': '联', '繫': '系',
    '辭': '辞', '彙': '汇', '為': '为', '廣': '广', '東': '东', '語': '语',
    '風': '风', '格': '格', '繁': '繁', '體': '体', '個': '个', '讀': '读',
    '緊': '紧', '按': '按', '鈕': '钮', '指': '指', '標': '标', '滑': '滑',
    '鼠': '鼠', '鍵': '键', '盤': '盘', '捷': '捷', '徑': '径', '暫': '暂',
    '儲': '储', '存': '存', '還': '还', '原': '原', '狀': '状', '恢': '恢',
    '復': '复', '正': '正', '在': '在', '複': '复', '習': '习', '完': '完',
    '整': '整', '高': '高', '效': '效', '閉': '闭', '環': '环', '離': '离',
    '開': '开', '預': '预', '複': '复', '深': '深', '入': '入', '鞏': '巩',
    '固': '固', '吸': '吸', '收': '收', '讓': '让', '孩': '孩', '子': '子',
    '更': '更', '好': '好', '地': '地', '學': '学', '習': '习', '新': '新',
    '任': '任', '班': '班', '主': '主', '任': '任', '豌': '豌', '豆': '豆',
}


def apply_localization(html):
    for old, new in GLOBAL_REPLACEMENTS:
        html = html.replace(old, new)
    # 粤语兜底（安全网，针对替换后仍可能残留的粤语字）
    for old, new in [
        ('嘅', '的'), ('咗', '了'), ('唔', '不'), ('係', '是'), ('冇', '没有'),
        ('喺', '在'), ('嚟', '来'), ('畀', '给'), ('咩', '什么'), ('乜', '什么'),
        ('蚊', '元'), ('喺', '在'), ('咁', '那么'), ('啲', '一些'),
    ]:
        html = html.replace(old, new)
    # 繁体 → 简体 字符映射
    for ch, simp in CHAR_MAP.items():
        html = html.replace(ch, simp)
    # 移除损坏字符（U+FFFD）
    html = html.replace('\ufffd', '')
    # 扩展循环：1..4 → 1..7
    html = html.replace('for (let i = 1; i <= 4; i++)', 'for (let i = 1; i <= 7; i++)')
    return html


# ---------------------------------------------------------------
# 校验
# ---------------------------------------------------------------
def check(html):
    problems = []
    if '台湾团队学员服务流程及话术' not in html:
        problems.append('课程标题未替换')
    if "'台湾团队学员服务流程及话术'" not in html:
        problems.append('courseData.title 未替换')
    if html.count("id: 's") != 8:
        problems.append('章节数不为 8（当前 sX 计数=%d）' % html.count("id: 's"))
    if html.count('quizId: \'quiz') != 7 and html.count('"quizId": "quiz') != 7:
        n = html.count('"quizId": "quiz')
        if n != 7:
            problems.append('quizId 数不为 7（当前=%d）' % n)
    for kw in ['微信', 'WhatsApp', '家長群', '建群', '學習群', '進群', '拉群', '群組', '群內', '好嘅', '我係', '哋']:
        if kw in html:
            problems.append('残留词：' + kw)
    for kw in ['課', '學', '話', '術', '開', '場', '題', '對', '評', '測', '檢', '維', '達', '蓋',
               '準', '確', '讀', '設', '結', '業', '證', '書', '習', '進', '時', '長', '記', '錄',
               '頻', '誤', '隱', '傳', '遞', '論', '練', '價', '審', '資', '監', '顧', '問', '訊',
               '讓', '請', '輸', '內', '後', '裡', '來', '們', '幫', '幾', '覺', '變', '歡', '該',
               '說', '認', '識', '點', '數', '圖', '運', '較', '單', '簡', '複', '預', '環', '閉',
               '歸', '標', '狀', '況', '鏈', '暫', '異', '議', '處', '續', '費', '規', '則', '詳',
               '節', '調', '籤', '觸', '連', '絡', '間', '聯', '號', '碼', '覽', '網', '頁', '軟',
               '體', '專', '務', '範', '親', '優', '饋', '筆', '綜', '過', '極', '輪', '擊', '擬',
               '發', '領', '滿', '獲', '補', '關', '當', '語', '總', '並', '於', '為', '與', '個',
               '這', '麼', '還', '會', '從', '現', '態', '據', '報', '導', '師', '選', '擇', '項',
               '錯', '訓', '劃', '職', '責', '繫', '辭', '彙', '廣', '東', '風', '繁', '緊',
               '鈕', '鍵', '盤', '徑', '儲']:
        if kw in html:
            problems.append('残留繁体/旧字：' + kw)
    if '__MIMO_API_KEY__' not in html:
        problems.append('缺少 _HEX2 密钥占位符（__MIMO_API_KEY__）')
    if 'api.deepseek.com' in html:
        problems.append('残留 DeepSeek 端点')
    if 'mimo-v2.5-pro' not in html:
        problems.append('缺少 MiMo 模型配置')
    if 'for (let i = 1; i <= 7; i++)' not in html:
        problems.append('交互循环未扩展为 7 章')
    return problems


def main():
    with open(TARGET, 'r', encoding='utf-8') as f:
        html = f.read()

    if '--check' in sys.argv:
        problems = check(html)
        if problems:
            print('[check] 未通过：')
            for p in problems:
                print('  - ' + p)
            sys.exit(1)
        print('[check] 通过：标题/章节/测验/AI配置/本地化检查全部通过。')
        return

    html = apply_blocks(html)
    html = apply_localization(html)

    with open(TARGET, 'w', encoding='utf-8') as f:
        f.write(html)

    problems = check(html)
    if problems:
        print('[build] 完成，但校验有告警：')
        for p in problems:
            print('  - ' + p)
        sys.exit(1)
    print('[build] 完成：index.html 已替换为台湾版，校验通过。')


if __name__ == '__main__':
    main()
