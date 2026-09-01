# -*- coding: utf-8 -*-
"""台湾版班导服务微课 — 内容数据（第3-4章）
内容严格来自 PPT《2-3台湾学员服务流程及话术【LP】.pptx》
本地化规则：LINE 替代微信、无家长群/建群服务、粤语改简体普通话
"""

SECTIONS_S34 = [
# ========== 第3章 专题&月度回访服务 ==========
{
  'id': 's3',
  'title': '专题&月度回访服务',
  'duration': '8-10分钟',
  'icon': '3',
  'type': 'content',
  'content': '''
<div class="section-header">
  <span class="section-badge">第三章</span>
  <h1>专题&月度回访服务</h1>
  <span class="duration">⏱ 预估时长 8-10 分钟</span>
</div>

<div class="card">
  <div class="card-title">📊 专题反馈</div>
  <table class="detail-table">
    <tr><th>项目</th><th>内容</th></tr>
    <tr><td>回访时间</td><td>首次专题结束后的 <strong>48小时内</strong></td></tr>
    <tr><td>回访频率</td><td><strong>2周1次</strong>（新生试学期）</td></tr>
    <tr><td>回访形式</td><td>电话回访 / LINE回访</td></tr>
  </table>
  <div class="highlight-box">
    <strong>反馈内容：</strong>
    <ul class="info-list" style="margin-top:8px;">
      <li>本专题所学知识重点文字描述 + 图片总结（运营按照专题、周维度提供模板）</li>
      <li>根据监课、课后看课，反馈至少1个学员闪光点和1个学习中问题点，并给出解决建议（根据看课结果进行反馈）</li>
      <li>至少向家长提一个问题，比如：课后孩子感觉学的怎么样等，确保与家长建立沟通关系，不是单方面的信息传递（确保双向沟通）</li>
      <li>下节课课程预告</li>
    </ul>
  </div>
</div>

<div class="card">
  <div class="card-title">📅 月度回访</div>
  <table class="detail-table">
    <tr><th>项目</th><th>内容</th></tr>
    <tr><td>回访频率</td><td><strong>每月1次</strong></td></tr>
    <tr><td>回访形式</td><td>电话</td></tr>
    <tr><td>名单来源</td><td>每月运营提供需月度回访的学员名单</td></tr>
    <tr><td>跟进标准</td><td>每个月跟进1次有效或3次无效</td></tr>
  </table>
  <div class="highlight-box warning">
    <strong>回访内容：</strong>
    <ul class="info-list" style="margin-top:8px;">
      <li>本月所学专题的内容及能力达成情况</li>
      <li>主动提问了解用户学习感受</li>
      <li>结合监课，反馈学员日常学习表现（薄弱点 + 进步点，侧重效果外化）</li>
      <li>学习规划</li>
      <li>异议处理，结束</li>
    </ul>
  </div>
  <div class="highlight-box">
    <strong>监控指标：</strong>
    <ul class="info-list" style="margin-top:8px;">
      <li>电话触达：follow 关键字「服务回访」，监控指标 follow，回访结果：已接通，通时 &gt; 3min</li>
      <li>LINE触达：follow 关键字「服务回访」，监控指标 follow，回访结果：已回复</li>
    </ul>
  </div>
</div>

<div class="highlight-box success">
  <strong>💡 回访要点：</strong>
  <ul class="info-list" style="margin-top:8px;">
    <li>效果外化：反馈薄弱点+进步点，侧重效果外化</li>
    <li>双向沟通：每个反馈点后主动询问家长看法</li>
    <li>问题导向：发现问题及时给出解决建议</li>
    <li>异议处理：及时处理并结束回访</li>
  </ul>
</div>

<!-- 嵌入式选择题 -->
<div id="quiz-quiz3"></div>

<!-- 嵌入式AI对话 -->
<div id="dialogue-quiz3"></div>
'''
},
# ========== 第4章 续费服务月回访 ==========
{
  'id': 's4',
  'title': '续费服务月回访',
  'duration': '8-10分钟',
  'icon': '4',
  'type': 'content',
  'content': '''
<div class="section-header">
  <span class="section-badge">第四章</span>
  <h1>续费服务月回访</h1>
  <span class="duration">⏱ 预估时长 8-10 分钟</span>
</div>

<div class="card">
  <div class="card-title">📋 续费服务月回访</div>
  <table class="detail-table">
    <tr><th>项目</th><th>内容</th></tr>
    <tr><td>回访时间</td><td>根据运营拆标逻辑特定池子</td></tr>
    <tr><td>回访频率</td><td><strong>续费前一个月</strong></td></tr>
    <tr><td>回访形式</td><td>电话回访 / LINE回访</td></tr>
  </table>
  <div class="highlight-box">
    <strong>回访内容：</strong>
    <ul class="info-list" style="margin-top:8px;">
      <li>过往学习内容及能力达成反馈</li>
      <li>根据监课、看课，反馈至少1个学员闪光点和1个学习中问题点，并给出解决建议（薄弱点 + 进步点，侧重效果外化）</li>
      <li>了解用户学习感受，及家长学习目标（确保双向沟通）</li>
      <li>异议处理，本级别或下个级别预告</li>
      <li>铺垫后续长期学习的规划</li>
    </ul>
  </div>
</div>

<div class="highlight-box success">
  <strong>💡 续费月回访要点：</strong>
  <ul class="info-list" style="margin-top:8px;">
    <li>效果外化：用过往学习成果与能力达成情况展示价值</li>
    <li>双向沟通：主动了解家长学习目标，确保双向沟通</li>
    <li>异议处理：处理异议后做本级别或下个级别预告</li>
    <li>长期规划：铺垫后续长期学习规划</li>
  </ul>
</div>

<!-- 嵌入式选择题 -->
<div id="quiz-quiz4"></div>

<!-- 嵌入式AI对话 -->
<div id="dialogue-quiz4"></div>
'''
},
]
