# -*- coding: utf-8 -*-
"""台湾版班导服务微课 — 内容数据（第1-2章）
内容严格来自 PPT《2-3台湾学员服务流程及话术【LP】.pptx》
本地化规则：LINE 替代微信、无家长群/建群服务、粤语改简体普通话
"""

SECTIONS_S12 = [
# ========== 第1章 首通流程（24小时） ==========
{
  'id': 's1',
  'title': '首通流程（24小时）',
  'duration': '15-20分钟',
  'icon': '1',
  'type': 'content',
  'content': '''
<div class="section-header">
  <span class="section-badge">第一章</span>
  <h1>首通流程（24小时）</h1>
  <span class="duration">⏱ 预估时长 15-20 分钟</span>
</div>

<div class="card">
  <div class="card-title">📋 通话前准备</div>
  <p style="margin-bottom:12px;">首通电话需在学员报名后 <strong>24小时内</strong> 完成。通话前需做好以下准备：</p>
  <div class="highlight-box">
    <strong>查看学员后台信息：</strong>
    <ul class="info-list" style="margin-top:8px;">
      <li>学员基本信息：姓名、性别、年龄、年级</li>
      <li>合同及课时详情：购课时间、价格、总课时数、是否有赠送</li>
      <li>学员排课信息：上课时间及首课时间，级别，授课老师信息，时差</li>
      <li>其他：例如课程顾问的跟进记录、是否已打卡、是否已提供转介绍或是被介绍学员等</li>
    </ul>
  </div>
  <div class="highlight-box warning">
    <strong>与课程顾问或教务老师交接：</strong>
    <ul class="info-list" style="margin-top:8px;">
      <li>确认后台学员基本信息，若有错误及时修改</li>
      <li>询问针对家长，是否有其他注意事项</li>
      <li>钉钉联系课程顾问若无回复，则根据自己时间安排先行联系家长</li>
    </ul>
  </div>
</div>

<div class="card">
  <div class="card-title">📞 首通电话流程（6步骤）</div>
  <div class="flow-steps">
    <div class="flow-step"><div class="step-num">1</div><h4>开场白</h4><p>自我介绍（我是谁、做什么、岗位职责）；表明来意，询问家长是否方便，说明大概时间5-10分钟，不方便则约定时间再去电（尽量约在24小时内）</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">2</div><h4>了解学员情况</h4><p>基本信息、报名初衷、过往学习经历、兴趣班及时间安排、决策人等；注意聆听家长反馈，充分互动</p></div>
  </div>
  <div class="flow-steps">
    <div class="flow-step"><div class="step-num">3</div><h4>确认课包具体内容</h4><p>课包价格、课时数（购买课时+赠送课时）、打卡次数；排课时间、首课时间、级别、语言、老师性别、课程时长、班型（6-8人）</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">4</div><h4>介绍家长端APP、服务号</h4><p>介绍家长端1-2个关键功能，引导家长下载安装；介绍VIP THINK服务号的功能，引导家长关注</p></div>
  </div>
  <div class="flow-steps">
    <div class="flow-step"><div class="step-num">5</div><h4>上课规则介绍</h4><p>结合VIP THINK学习闭环，从学习习惯和学习效果出发，告知请假-补课-停课-旷课的规则，注意沟通方式，减少异议</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">6</div><h4>转介绍福利、升舱铺垫</h4><p>介绍打卡规则和转介绍老带新福利，家长不参加打卡不要勉强，说清活动即可；铺垫升舱活动</p></div>
  </div>
</div>

<div class="card">
  <div class="card-title">💬 开场白话术参考</div>
  <div class="script-block">
    <p><span class="lp-line">LP:</span> XX妈妈/爸爸您好？我是VIP THINK的班导XX老师，很高兴可以跟您电话沟通。您报名了我们的课程，分配到我的班级，以后小朋友在VIP THINK的学习，都会由我全程负责跟进喔。请问您现在方便接电话吗？</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 方便</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 今天打给您，主要想跟您确认上课相关信息，说一下开课的注意事项，也想了解一下小朋友的基础情况，这样我们可以更好地帮助小朋友在VIP THINK学习和成长。</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 您说</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 首先跟您介绍一下我们VIP THINK的课程设置。课程采用真人在线授课小班课，双师教学模式，平时除了授课老师和小朋友上课，还会有我们班导负责小朋友的日常学习跟进。平时除了每周2次的主修课，假期和寒暑假我们还会安排针对性的主题课程（寒暑假会有计算班和数独班）。我会定期跟您反映小朋友在VIP THINK的学习情况，如果小朋友学习中遇到数学相关的困难或者挑战，又或者对课程和老师有什么想法或建议，都可以随时联系我。</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 好的，谢谢您</p>
  </div>
</div>

<div class="card">
  <div class="card-title">💬 学员状况了解/期望话术参考</div>
  <div class="script-block">
    <p><span class="lp-line">LP:</span> XX小朋友今年是XX岁对吗？是男生还是女生呢？现在是读XX年级，对吗？</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 我想了解一下，我们小朋友之前有没有在课外上过数学思维课，或者家里爸爸妈妈有没有买过一些相关的书给小朋友了解一下？</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 没学过，第一次接触思维课</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> （可以根据课程大纲问）这样小朋友会认数和点数20以内的数吗？认识基础平面图形吗？可以熟练计算20以内的加减吗？</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 会一点点数，但加减还不会</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 小朋友平时愿不愿意主动表达？性格是偏慢热还是比较活泼？平时是用短语还是句子来表达呢？</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 正常沟通是可以的，有些慢热</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 明白，小朋友整体水平都不错。妈妈这次报名思维课，想提升小朋友哪方面的能力呢？</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 打好数学基础，计算提高下就更好</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 明白妈妈，我们的课程每四节课一个专题，会针对性强化小朋友的思维和数学，小朋友在VIP THINK学习一定会有进步的。顺便了解一下，我们小朋友现在除了VIP THINK课之外，还有没有上其他课外班？</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 学的都是兴趣类课程，数学课就这一门</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 通过跟妈妈的沟通，小朋友的基本情况我都了解得差不多了，看来妈妈平时对小朋友的学习和教育都很重视。这样爸爸平时有空会不会跟您一起负责小朋友学习？</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 主要由我负责小朋友学习</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> （无论参不参与）每节课后我都会在LINE上向您反馈小朋友的学习情况，也可以同步给爸爸一起了解。小朋友的情况我都做了记录，我也会跟我们的授课老师说一下，让老师可以根据小朋友的性格和兴趣调整上课方式，激发小朋友兴趣。接着跟妈妈确认一下您比较关心的课程问题。</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 谢谢</p>
  </div>
  <div class="highlight-box">
    <strong>💡 能力摸底维度：</strong>识数（口头数、点物数、计数）｜运算（加减、进退位、混合运算、乘除）｜空间图形（平面、立体、展开图、周长面积）｜表达能力（关键词→完整句→清晰流畅→逻辑→用词丰富）
  </div>
</div>

<div class="card">
  <div class="card-title">📋 核对课程信息要点</div>
  <table class="detail-table">
    <tr><th>项目</th><th>需确认内容</th></tr>
    <tr><td>课时包</td><td>总课时（购买课时+赠送课时）、打卡次数、课程有效期、价格</td></tr>
    <tr><td>上课安排</td><td>排课时间、首课时间、级别、语言、老师性别、课程时长（40分钟）、班型（6-8人）</td></tr>
    <tr><td>APP安装</td><td>学生端+家长端APP、账号（手机号）、初始密码（123456）</td></tr>
    <tr><td>课后环节</td><td>课后巩固（约5-6题）、小老师录像环节</td></tr>
  </table>
  <div class="script-block" style="margin-top:18px;">
    <strong>💬 核对课包参考话术：</strong><br>
    「我们在X月X日报名了VIP THINK的<strong>XX课时包</strong>，另外赠送X课时，一共是X课时，以及XX次打卡次数。打卡需要上传到<strong>LINE动态</strong>，需要打卡XX周，每周打卡会获得2000豌豆币，8000豌豆币可以兑换一节课程，一共是XX元，课程有效期是XX，您看一下对不对喔？小朋友的课程是由<strong>SX这个级别</strong>开始，授课语言是XX，上课时间是每周X和周X的<strong>XX:XX</strong>，第一次上课是周X晚上XX:XX分，每节课<strong>40分钟</strong>，我们这个班有XX人，妈妈记得设好闹钟喔，准时到课喔。」
  </div>
</div>

<div class="card">
  <div class="card-title">⚠️ 请假 / 休学 / 旷课规则（重要）</div>
  <div class="highlight-box danger">
    <table class="detail-table" style="margin:0;">
      <tr><th>规则</th><th>具体内容</th></tr>
      <tr><td>请假</td><td>提前24小时在家长端申请；家长端最迟课前三小时自行操作，班导最迟课前1小时操作；课包内含XX次免费请假机会，请假机会内请假不扣课时</td></tr>
      <tr><td>补课</td><td>请假后及时补课，直播补课之后才扣除相应课时；超过免费次数后请假会正常扣课时，后期对应安排免费回放补课</td></tr>
      <tr><td>休学</td><td>一次休学机会，最长30天，不保留原班级学位，复课后需重新安排课程，最好提前三天办理</td></tr>
      <tr><td>旷课</td><td>当节课没出席又没提前请假或休学，系统自动记为旷课，课时正常扣除</td></tr>
    </table>
  </div>
  <div class="script-block" style="margin-top:18px;">
    <strong>💬 请假规则参考话术：</strong><br>
    <div style="margin-top:8px;line-height:1.8;">
      <strong>① 请假：</strong>「妈妈可以提前24小时在家长端里帮小朋友申请请假，如果到时不方便都可以告诉我，我这边都可以操作。家长端最迟可以课前三小时您自己操作，我最迟可以课前1小时操作，都来得及。在请假机会内请假是不会扣除课时的，不过为了小朋友更好衔接后面的学习内容，我建议请假后要及时补课。超过次数之后，如果有事请假都可以，不过会正常扣除课时，后期会对应安排免费回放补课，辛苦妈妈带着小朋友学习，如果有不懂可以随时在LINE上问老师，及时解决问题。」<br><br>
      <strong>② 休学：</strong>「另外考虑到小朋友后期可能会有特殊情况需要休学，我们也给小朋友一次休学机会，最长休学时间是30天，不过休学是不保留原有班级学位，复课后需要重新安排课程。这种情况发生得很少，但都跟您说一声，最好提前三天办理。」<br><br>
      <strong>③ 旷课：</strong>「如果小朋友当节课没出席，又没提前请假或休学，系统会自动记为小朋友旷课，课时会正常扣除，妈妈千万不要忘记。」
    </div>
  </div>
</div>

<div class="card">
  <div class="card-title">📱 介绍家长端 & VIP THINK服务号</div>
  <ul class="info-list">
    <li><strong>学生端APP：</strong>上课使用，课前预热影片环节（课前几分钟可提前看）</li>
    <li><strong>家长端APP重点功能：</strong>首页"小老师影片"（每节课后上传录像）、底部"课程"图示（预热/上课/内容巩固）、"在线旁听"按钮</li>
    <li><strong>账号密码：</strong>学生端和家长端都用报名手机号登入，初始密码123456，建议登入后尽快修改</li>
    <li><strong>服务号：</strong>VIP THINK服务号，自动发送上课提醒，发布最新福利活动</li>
  </ul>
  <div class="script-block" style="margin-top:18px;">
    <strong>💬 介绍APP & 服务号参考话术：</strong><br>
    「上课会用『<strong>VIP THINK学生端</strong>』APP，您作为家长就需要下载『<strong>VIP THINK家长端</strong>』APP。这个家长端很好用，我跟您说一下重点功能：首页『<strong>小老师影片</strong>』，每节课后会有个小任务，请小朋友做小老师讲解一道题，您帮忙录下来上传，这样可以加深他的理解和表达能力喔；底部『<strong>课程</strong>』图示，里面可以看到每节课的『预热一下』『上课』和『内容巩固』情况，到上课时间您会看到『<strong>在线旁听</strong>』的按钮，点进去就可以远程看到小朋友上课实况。账号密码：学生端和家长端都用您报名的手机号登入，初始密码是123456，为了安全，建议您登入后尽快修改密码。妈妈有没有用LINE呀？（若家长有LINE）那我加您一下LINE，稍后发送『VIP THINK服务号』的信息给您，请您关注。服务号会自动发送上课提醒，也发布最新福利活动，不会错过重要信息喔。」
  </div>
</div>

<div class="card">
  <div class="card-title">🎁 福利介绍（打卡与转介绍）</div>
  <div style="display:flex;gap:16px;flex-wrap:wrap;">
    <div style="flex:1;min-width:200px;background:var(--card);border:2px solid var(--border);border-radius:var(--radius-sm);padding:20px;text-align:center;box-shadow:var(--shadow);">
      <div style="font-size:32px;margin-bottom:8px;">📝</div>
      <h4 style="font-size:15px;font-weight:700;">打卡福利</h4>
      <p style="font-size:13px;color:var(--text-secondary);">每周在LINE动态或FB等打卡1次（用家长端生成的专属海报），获得2000豌豆币；8000豌豆币可兑换一节直播课</p>
    </div>
    <div style="flex:1;min-width:200px;background:var(--card);border:2px solid var(--border);border-radius:var(--radius-sm);padding:20px;text-align:center;box-shadow:var(--shadow);">
      <div style="font-size:32px;margin-bottom:8px;">🤝</div>
      <h4 style="font-size:15px;font-weight:700;">转介绍福利</h4>
      <p style="font-size:13px;color:var(--text-secondary);">朋友（3-12岁）扫您海报上的QR Code登记试听，试听完成获得额外豌豆币；朋友报名获赠更多课时</p>
    </div>
    <div style="flex:1;min-width:200px;background:var(--card);border:2px solid var(--border);border-radius:var(--radius-sm);padding:20px;text-align:center;box-shadow:var(--shadow);">
      <div style="font-size:32px;margin-bottom:8px;">🚀</div>
      <h4 style="font-size:15px;font-weight:700;">升舱权益</h4>
      <p style="font-size:13px;color:var(--text-secondary);">每个级别96节课，开课3个月内可补差价优惠价规划完整级别学习，比正常续费便宜2000-3000元</p>
    </div>
  </div>
  <div class="script-block" style="margin-top:18px;">
    <strong>💬 福利介绍参考话术：</strong><br>
    「另外有两个福利等着您和小朋友：<strong>打卡福利</strong>，每周在社交软件上，譬如LINE动态或者FB等，打一次卡（用家长端生成的专属海报），完成后就可以获得<strong>2000豌豆币</strong>，豌豆币可以在商城兑换直播课，很实用。记得打卡完成24小时后要截图上传回去APP，系统会很快审核。<strong>转介绍福利</strong>，如果您有朋友的小朋友（3-12岁）对思维课有兴趣，可以请他扫您海报上的QR Code登记试听，朋友完成试听，您就会获得额外豌豆币（例如每月邀请1位，最少有24000豌豆币），如果朋友报名，您还会获赠更多课时。」
  </div>
</div>

<div class="card">
  <div class="card-title">💬 升舱权益预告＆结束语</div>
  <div class="script-block">
    <p><span class="lp-line">LP:</span> 最后一点是关于您的专属权益。我们每个级别总共有96节课，每位新生都有一个特别福利：在开课起三个月内，您可以透过补差价的方式，以优惠价为小朋友规划完整级别的学习。这个专属价比正常续费大概便宜2000-3000元，也是唯一一次最低单价的机会。您现在可以先了解一下，等小朋友上了几节课，适应得好的话，我在权益截止前再跟您详细商量。</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> OK，我今天讲的内容就这么多了，您有没有其他问题想问呢？</p>
    <p style="margin-top:8px;"><span class="parent-line">家长:</span> 暂时没有，老师</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 好的，今后小朋友上课有任何问题，都由我负责跟进。我已经加了您LINE，后续授课老师也会通过LINE和您保持联系，方便沟通。另外提醒一下，我通常星期一休息，如果当日回复慢了，请多多包涵。有紧急情况可以直接打我电话。</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 很高兴跟您聊天，我们保持联系，第一节课后我再跟您跟进小朋友的情况。再见！</p>
  </div>
</div>

<div class="card">
  <div class="card-title">💬 LINE服务留言</div>
  <p style="margin-bottom:12px;">首通电话结束后，通过LINE向家长发送服务留言，保持服务衔接：</p>
  <ul class="info-list">
    <li>发送首课上课提醒（首课时间、上课内容、设备与网络检查）</li>
    <li>告知班导休息日（通常星期一），回复稍慢请家长见谅</li>
    <li>有紧急情况可直接打电话联系班导</li>
  </ul>
</div>

<div class="card">
  <div class="card-title">📋 首通服务流程总结</div>
  <div class="flow-steps">
    <div class="flow-step"><div class="step-num">1</div><h4>通话前准备</h4><p>查看后台信息 + 与顾问/教务交接</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">2</div><h4>开场白</h4><p>自我介绍、表明来意、确认方便</p></div>
  </div>
  <div class="flow-steps">
    <div class="flow-step"><div class="step-num">3</div><h4>了解学员情况</h4><p>基本信息、能力摸底、性格与期望</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">4</div><h4>核对课包</h4><p>课时包、上课安排、APP安装、课后环节</p></div>
  </div>
  <div class="flow-steps">
    <div class="flow-step"><div class="step-num">5</div><h4>介绍家长端与服务号</h4><p>关键功能 + 加LINE + 关注服务号</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">6</div><h4>上课规则与福利</h4><p>请假/休学/旷课规则 + 打卡/转介绍福利 + 升舱铺垫</p></div>
  </div>
  <div class="highlight-box success">
    <strong>✅ 首通完成后：</strong>通过LINE发送服务留言（上课提醒模板），告知休息日与紧急联系方式，24小时内完成首通。
  </div>
</div>

<!-- 嵌入式选择题 -->
<div id="quiz-quiz1"></div>

<!-- 嵌入式AI对话 -->
<div id="dialogue-quiz1"></div>
'''
},
# ========== 第2章 首课回访（48小时） ==========
{
  'id': 's2',
  'title': '首课回访（48小时）',
  'duration': '10-15分钟',
  'icon': '2',
  'type': 'content',
  'content': '''
<div class="section-header">
  <span class="section-badge">第二章</span>
  <h1>首课回访（48小时）</h1>
  <span class="duration">⏱ 预估时长 10-15 分钟</span>
</div>

<div class="card">
  <div class="card-title">📱 课前LINE提醒（3步骤）</div>
  <div class="flow-steps">
    <div class="flow-step"><div class="step-num">1</div><h4>提醒首课及注意事项</h4><p>告知家长首课时间及第一节课上课内容（确认是否有误、是否可以到课）；确认设备和网络是否正常还有APP下载</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">2</div><h4>介绍学习闭环</h4><p>简单介绍VIP THINK学习闭环，重点强调预习</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">3</div><h4>确认寄收地址</h4><p>确认收货地址是否填写完整</p></div>
  </div>
</div>

<div class="card">
  <div class="card-title">👀 首课监课</div>
  <div class="highlight-box">
    <p>首课进行时，班导需提前安排好自己的工作时间，务必重视新学员的首课；如同时有2-3个新生需监课，协调好时间。监课要点：</p>
    <ul class="info-list" style="margin-top:8px;">
      <li>提前5分钟进入教室，确保学生老师同时进入教室，设备无误，课件显示正常</li>
      <li>切实感受课中老师与学生互动情况，为课后回访丰富内容</li>
      <li>关注学员课堂表现，观察师生互动情况，高光时刻反馈</li>
      <li>如出现设备问题，可协助联系IT及时解决（学生端、监课端、后台建工单）</li>
      <li>做好监课记录</li>
    </ul>
  </div>
</div>

<div class="card">
  <div class="card-title">📞 首课后回访概览</div>
  <table class="detail-table">
    <tr><th>项目</th><th>内容</th></tr>
    <tr><td>回访目的</td><td>跟进学员上课感受，及时处理异议问题；督促学生养成良好学习习惯</td></tr>
    <tr><td>回访时间</td><td>首课结束后 <strong>48小时内</strong></td></tr>
    <tr><td>回访准备</td><td>与授课老师沟通学员首课学情；查看学员首课报告，并复制链接给家长</td></tr>
    <tr><td>回访方式</td><td>电话回访</td></tr>
  </table>
</div>

<div class="card">
  <div class="card-title">📋 首课后回访流程（5步骤）</div>
  <div class="flow-steps">
    <div class="flow-step"><div class="step-num">1</div><h4>开场白</h4><p>表明身份、明确来电目的，询问是否方便</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">2</div><h4>学员课堂适应</h4><p>了解家长对首课的满意度</p></div>
  </div>
  <div class="flow-steps">
    <div class="flow-step"><div class="step-num">3</div><h4>监课情况及老师反馈</h4><p>反馈学员课堂表现，解读首课报告，了解家长对老师的满意度</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><div class="step-num">4</div><h4>强调课后</h4><p>提醒复习，及时完成课后作业，强调陪伴式教育</p></div>
  </div>
  <div class="flow-steps">
    <div class="flow-step"><div class="step-num">5</div><h4>处理异议与结束语</h4><p>处理家长异议问题，确认无其他问题后结束</p></div>
  </div>
</div>

<div class="card">
  <div class="card-title">💬 回访话术参考</div>
  <div class="script-block">
    <p><span class="lp-line">LP:</span> XX妈妈，您好，我是VIP THINK的班导XXX老师。我们小朋友已经在VIP THINK完成了自己的第一次正式课程学习，今天给您来电是想第一时间跟您沟通一下我们小朋友的上课情况。</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 我们小朋友第一次上课，您有在旁边陪伴他一起上课吗？您观察下来或者课后跟小朋友沟通下来，对于课程难易程度觉得能接受吗？（比较顺畅→表扬为主→进入第三步；偏简单→表扬学员优点，突出优势，讲解本节课内容，分析原因，不要轻易提出升阶；偏难→突出学员优秀的地方，讲解本节课内容，分析原因，不要轻易提出降阶）有些小朋友可能第一次上课会有一些紧张或者还没有完全适应，我们小朋友第一节课整个过程还适应吗？</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 这节课我也去监课了，课堂上老师每次对我们小朋友提问的时候，孩子表现还是比较害羞的/积极的，同时整节课专注度还是不错。</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> （结合首课报告解读）小朋友这个专题学习的是巧解格阵的知识，本节课是这个专题的第一节课，本节课结合形状和物品组合，引导幼儿去发现两者结合的规律，再运用规律辨识完成相应物品的摆放，通过这种一一对应的过程，帮助孩子熟练应用对应关系解决问题，培养幼儿的对应思维和迁移与应用的能力。建议家长课后可以通过摆放小物件，创造位置对应关系，帮助孩子巩固课堂知识，进一步培养孩子的对应思维。这节课主要涉及到孩子观察力、分析能力、推理能力的培养。本节课孩子课堂答对了8道题，正确率80%呢。课后练习也已经完成了，正确率是100%。说明小朋友这节课知识掌握的非常好，而且观察能力、分析能力和推理能力的训练都很不错哦。</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 相信妈妈在关注小朋友上课状态的同时，妈妈一定也关注了老师的授课情况。孩子对老师还喜欢吧？（认可→向家长介绍老师；不认可→异议处理，后续跟进）</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> XX妈妈，我们每次上完课以后，本节课的内容是可以进行复习的，就在孩子上课的客户端里面，我们可以带小朋友再回顾1次上课课件动画，包括上课中老师教过的小题目，可以让小朋友再自己独立完成1次。回顾完了以后，还有1个课后作业，很简单，只有几个小题目，可以让小朋友及时进行巩固。以后每次上完课，您记得都可以让小朋友进行复习和课后作业的练习，以保证我们每次课程内容的吸收，同时也可以养成孩子良好的学习习惯。其实题目都挺简单的，孩子如果有不是很会的，妈妈您指导他的时候也不用太着急，还是要多以鼓励为主。到时候您可以把情况反馈给我，我会跟老师沟通，让老师重点注意下他还不太熟练的内容。</p>
    <p style="margin-top:8px;"><span class="lp-line">LP:</span> 妈妈您这边还有什么其他问题吗？（等待家长回答，有问题行异议处理或常规回答）妈妈之后我们有问题可以再LINE联系我，要是没有及时回复，您就打我电话，妈妈再见。</p>
  </div>
</div>

<div class="highlight-box success">
  <strong>✅ 回访要点：</strong>
  <ul class="info-list" style="margin-top:8px;">
    <li>先与授课老师沟通，了解学员首课学情</li>
    <li>查看学员首课报告，复制链接发给家长</li>
    <li>反馈至少1个闪光点和1个可提升点</li>
    <li>强调课后巩固和学习闭环，督促学习习惯养成</li>
    <li>确保双向沟通，不是单方面信息传递</li>
  </ul>
</div>

<!-- 嵌入式选择题 -->
<div id="quiz-quiz2"></div>

<!-- 嵌入式AI对话 -->
<div id="dialogue-quiz2"></div>
'''
},
]
