---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I graduated from EE College, Zhejiang University (浙江大学电气学院) with a bachelor’s degree and now studying for PhD in <a href="http://usslab.org">USSLAB</a>, advised by Prof. <a href="https://sites.google.com/site/xiaoyuijh/home">Xiaoyu Ji (冀晓宇)</a> and Prof. <a href="https://sites.google.com/view/xuwenyuan/">Wenyuan Xu (徐文渊)</a>.

My research focuses on embodied AI security and safety, especially in the following research directions:

- **Red-teaming for Embodied AI**: uncovering how embodied AI systems can be steered into unsafe behavior, and measuring comprehensive risks across perception, planning, and execution.
- **Safety Alignment for Embodied AI**: extending safety alignment from LLMs/VLMs to VLAs/WAMs, so that embodied AI systems act in accordance with human values.
- **Defense for Embodied AI Systems**: building safeguards across the whole pipeline, from proactive filtering of unsafe inputs to post-hoc detection of unsafe behavior.

My work has appeared in security and AI venues including NDSS, ACM CCS, AAAI, and WWW. I have published 6 papers at CCF-A conferences with total <a href='https://scholar.google.com/citations?user=cz6jVd0AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

# 🔥 News
- *2026.07*: &nbsp;🎉🎉 NDSS 2027, Easier Said Than Done: Unpacking the Intent–Behavior Gap in Jailbreaking LLM-based Robots.
- *2026.04*: &nbsp;🎉🎉 CCS 2026, GhostTac: Manipulating Tactile Sensors without Physical Contact.
- *2025.11*: &nbsp;🎉🎉 AAAI 2026, Phantom Menace: Exploring and Enhancing the Robustness of VLA Models against Physical Sensor Attacks.
- *2024.09*: &nbsp;🎉🎉 NDSS 2025, PhantomLiDAR: Cross-modality Signal Injection Attacks against LiDAR.
- *2024.01*: &nbsp;🎉🎉 WWW 2024, Unity is Strength? Benchmarking the Robustness of Fusion-based 3D Object Detection against Physical Sensor Attack.
- *2023.09*: &nbsp;🎉🎉 NDSS 2024, Inaudible Adversarial Perturbation: Manipulating the Recognition of User Speech in Real Time. 

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NDSS 2027</div><img src='images/POEF.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="paper-title">Easier Said Than Done: Unpacking the Intent–Behavior Gap in Jailbreaking LLM-based Robots</div>

**Xuancun Lu**, Zhengxian Huang, Xinfeng Li, Chi Zhang, Xiaoyu Ji, Wenyuan Xu

<div class="paper-links">
<a href="https://arxiv.org/abs/2412.16633"><i class="ai ai-arxiv"></i>Paper</a>
<a href="https://zjushine.github.io/poef.github.io/"><i class="fas fa-globe"></i>Homepage</a>
<a href="https://github.com/ZJUshine/POEF"><i class="fab fa-github"></i>Code</a>
<a href="https://github.com/ZJUshine/Harmful-Behavior"><i class="fas fa-database"></i>Dataset</a>
</div>

- We reveal an *intent–behavior gap* in jailbreaking LLM-based robots: malicious-looking policies rarely translate into harmful physical executions, because existing attacks overlook robot-specific syntax constraints and physical feasibility. We propose POEF, an automated red-teaming framework that embeds these constraints into both prompt optimization and evaluation, achieving an 80% behavior jailbreak success rate on the Unitree G1, the Franka arm, and simulators, and we present two defenses.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CCS 2026</div><img src='images/GhostTac.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="paper-title">GhostTac: Manipulating Tactile Sensors without Physical Contact</div>

Kun Wang, **Xuancun Lu**, Ruochen Zhou, Kai Wang, Tongjun Ye, Yihao Shao, Chen Yan, Xiaoyu Ji, Wenyuan Xu

<div class="paper-links">
<a href="https://arxiv.org/abs/2608.20817"><i class="ai ai-arxiv"></i>Paper</a>
<a href="https://ghosttac.github.io/GhostTacCCS.io/"><i class="fas fa-globe"></i>Homepage</a>
</div>

- We present GhostTac, the first contactless attack that manipulates tactile sensing via electromagnetic interference (EMI). By exploiting nonlinear rectification and limited-bandwidth amplification, crafted EMI signals become a persistent DC offset that bypasses on-board filtering, enabling fine-grained control over sensor outputs and inducing harmful robot behaviors such as excessive grasping force. We validate GhostTac on 15 tactile sensors across 10 modules and 2 dexterous hands, with case studies on grasping, slip detection, and material classification.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='images/PhantomMenace.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="paper-title">Phantom Menace: Exploring and Enhancing the Robustness of VLA Models against Physical Sensor Attacks</div>

**Xuancun Lu**, Jiaxiang Chen, Shilin Xiao, Zizhi Jin, Zhangrui Chen, Hanwen Yu, Bohan Qian, Ruochen Zhou, Xiaoyu Ji, Wenyuan Xu

<div class="paper-links">
<a href="https://arxiv.org/abs/2511.10008"><i class="ai ai-arxiv"></i>Paper</a>
<a href="https://ojs.aaai.org/index.php/AAAI/article/view/40881"><i class="fas fa-book"></i>Proceedings</a>
<a href="https://github.com/ZJUshine/Phantom-Menace"><i class="fab fa-github"></i>Code</a>
</div>

<strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We present the first systematic study of physical sensor attacks against Vision-Language-Action (VLA) models. Our "Real-Sim-Real" framework automatically simulates six camera attacks and two microphone attacks and validates them on real robots, exposing vulnerabilities whose severity depends critically on task type and model design. We further develop an adversarial-training-based defense that improves robustness to these out-of-distribution perturbations while preserving model performance.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NDSS 2025</div><img src='images/PhantomLiDAR.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="paper-title">PhantomLiDAR: Cross-modality Signal Injection Attacks against LiDAR</div>

Zizhi Jin, Qinhong Jiang, **Xuancun Lu**, Chen Yan, Xiaoyu Ji, Wenyuan Xu

<div class="paper-links">
<a href="https://arxiv.org/abs/2409.17907"><i class="ai ai-arxiv"></i>Paper</a>
<a href="https://sites.google.com/view/phantomlidar"><i class="fas fa-globe"></i>Homepage</a>
</div>

<strong><span class='show_paper_citations' data='cz6jVd0AAAAJ:d1gkVwhDpl0C'></span></strong>
- We show that a LiDAR's laser receiving circuit, monitoring sensors, and beam-steering modules still couple with intentional electromagnetic interference (IEMI) despite strict EMC testing. Exploiting these attack surfaces, PhantomLiDAR achieves Points Interference, Injection, Removal, and even LiDAR Power-Off, demonstrated on five COTS LiDARs in both simulated and real-world moving scenarios, along with sensor- and vehicle-level defenses.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WWW 2024</div><img src='images/PSA-Fusion.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="paper-title">Unity is Strength? Benchmarking the Robustness of Fusion-based 3D Object Detection against Physical Sensor Attack</div>

Zizhi Jin, **Xuancun Lu**, Bo Yang,Yushi Chen, Chen Yan, Xiaoyu Ji, Wenyuan Xu

<div class="paper-links">
<a href="https://zjushine.github.io/PSA-Fusion/"><i class="fas fa-globe"></i>Homepage</a>
<a href="https://github.com/Jinzizhisir/PSA-Fusion/"><i class="fab fa-github"></i>Code</a>
</div>

<strong><span class='show_paper_citations' data='cz6jVd0AAAAJ:u-x6o8ySG0sC'></span></strong>
- Our new benchmark features 5 types of LiDAR attacks and 6 types of camera attacks. Different from traditional benchmarks, we take the physical sensor attacks into consideration during the corruption construction. Then, we systematically investigate 7 MSF-based and 5 single-modality 3D object detection models with different fusion architectures.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NDSS 2024</div><img src='images/IAP-500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="paper-title">Inaudible Adversarial Perturbation: Manipulating the Recognition of User Speech in Real Time</div>

Xinfeng Li, Chen Yan, **Xuancun Lu**, Zihan Zeng, Xiaoyu Ji, Wenyuan Xu

<div class="paper-links">
<a href="https://arxiv.org/abs/2308.01040"><i class="ai ai-arxiv"></i>Paper</a>
<a href="https://github.com/LetterLiGo/Adversarial_Audio_Attack-VRifle"><i class="fab fa-github"></i>Code</a>
</div>

<strong><span class='show_paper_citations' data='cz6jVd0AAAAJ:u5HHmVD_uO8C'></span></strong>
- We propose VRIFLE, an inaudible adversarial perturbation (IAP) attack via ultrasound delivery that can manipulate ASRs as a user speaks. 
</div>
</div>


# 📖 Educations
- *2023.06 - now*, PhD, USSLAB, EE College, Zhejiang Univeristy, Hangzhou.
- *2019.09 - 2023.06*, Undergraduate, EE College, Zhejiang Univeristy, Hangzhou.

# 🧑‍⚖️ Services
- Reviewer, AAAI Conference on Artificial Intelligence (AAAI).

<!-- # 🎖 Honors and Awards -->
<!-- - *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->
<!-- # 💬 Invited Talks -->
<!-- - *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->
<!-- - *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->


<!-- # 💻 Internships -->
<!-- - *2019.05 - 2020.02*, [Lorem](https://github.com/), China. -->
