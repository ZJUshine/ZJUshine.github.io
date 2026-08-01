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

My research interest includes the embodied AI security and safety. I have published 6 paper at the CCF-A conferences with total <a href='https://scholar.google.com/citations?user=cz6jVd0AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

# 🔥 News
- *2026.07*: &nbsp;🎉🎉 NDSS 2027, Easier Said Than Done: Unpacking Intent–Behavior Gap in Jailbreaking LLM-based Robot.
- *2026.04*: &nbsp;🎉🎉 CCS 2026, GhostTac: Manipulating Tactile Sensors without Physical Contact.
- *2025.11*: &nbsp;🎉🎉 AAAI 2026, Phantom Menace: Exploring and Enhancing the Robustness of VLA Models against Physical Sensor Attacks.
- *2024.09*: &nbsp;🎉🎉 NDSS 2025, PhantomLiDAR: Cross-modality Signal Injection Attacks against LiDAR.
- *2024.01*: &nbsp;🎉🎉 WWW 2024, Unity is Strength? Benchmarking the Robustness of Fusion-based 3D Object Detection against Physical Sensor Attack.
- *2023.09*: &nbsp;🎉🎉 NDSS 2024, Inaudible Adversarial Perturbation: Manipulating the Recognition of User Speech in Real Time. 

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NDSS 2027</div><img src='images/POEF.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="paper-title">Easier Said Than Done: Unpacking Intent–Behavior Gap in Jailbreaking LLM-based Robot</div>

**Xuancun Lu**, Zhengxian Huang, Xinfeng Li, Chi Zhang, Xiaoyu Ji, Wenyuan Xu

- LLM-based robots use Large Language Models (LLMs) as planners to translate natural language instructions into policies such as `grasp()`, `move_to()`, and `open_gripper()`. Jailbreak attacks on these robots extend the threat from *generating malicious content* to *executing harmful behaviors*. However, we find that existing jailbreak attempts against LLM-based robots produce malicious-looking policies (*intent jailbreaks*) often fail to induce harmful robot physical executions (*behavior jailbreaks*), due to the robot-specific constraints, such as logical errors, hallucinated control APIs, etc. In this paper, we demystify the intent-behavior gap and investigate its root causes to inform effective defenses. Our measurement study finds that current LLM jailbreak methods overlook robot-specific syntax constraints (e.g., executable control APIs) and physical feasibility (e.g., orders of policies and hardware/kinematic constraints). To bridge the gap, we introduce POEF (**PO**licy **EF**fective Jailbreak), an automated red-teaming framework that takes into account the robot-specific constraints during both the optimization and evaluation process. Specifically, POEF employs the hidden-layer gradients from an unaligned LLM to guide the jailbreak prompt optimization and uses a multi-agent evaluator to assess the feasibility of the generated policies. Experiments on commercial robots, including the Unitree G1, the Franka robotic arm, and simulators, show that POEF achieves an 80% behavior jailbreak success rate and transfers across various LLMs. In addition, we propose two defense strategies that mitigate the behavior jailbreak risks. Our findings indicate an urgent need for stronger countermeasures before LLM-based robots are deployed at scale.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CCS 2026</div><img src='images/GhostTac.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="paper-title">GhostTac: Manipulating Tactile Sensors without Physical Contact</div>

Kun Wang, **Xuancun Lu**, Ruochen Zhou, Kai Wang, Tongjun Ye, Yihao Shao, Chen Yan, Xiaoyu Ji, Wenyuan Xu

- Tactile sensors are integral components of modern robotic systems, enabling robots to perceive and interact with the physical environment through tactile feedback. Despite their importance, the physical-layer security of tactile sensors has received little attention in prior work. In this paper, we present GhostTac, to the best of our knowledge, the first contactless attack that manipulates tactile sensing via electromagnetic interference (EMI). We identify that EMI exploits the nonlinear rectification and limited bandwidth amplification effects, allowing carefully crafted EMI signals to be converted into a persistent DC offset that bypasses on-board filtering and induces stable measurement deviations. Building on this mechanism, GhostTac enables fine-grained and controllable manipulation of sensor outputs by reshaping the spatial distribution and manipulating the magnitude at the targeted location. Such interference can induce unintended and harmful robot behaviors, such as causing a domestic robot to exert excessive force, resulting in physical damage or human injury. We evaluate GhostTac on 10 sensor modules and 2 dexterous hands, covering 15 tactile sensors of different types, and demonstrate consistent attack effectiveness across all tested devices. We further present three case studies on tactile grasping, slip detection, and material classification to illustrate practical impacts in real robotic tasks. We envision that our findings shed light on a new physical attack vector against tactile sensing in robotic systems.
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
- Vision-Language-Action (VLA) models revolutionize robotic systems by enabling end-to-end perception-to-action pipelines that integrate multiple sensory modalities, such as visual signals processed by cameras and auditory signals captured by microphones. This multi-modality integration allows VLA models to interpret complex, real-world environments using diverse sensor data streams. Given the fact that VLA-based systems heavily rely on the sensory input, the security of VLA models against physical-world sensor attacks remains critically underexplored. To address this gap, we present the first systematic study of physical sensor attacks against VLAs, quantifying the influence of sensor attacks and investigating the defenses for VLA models. We introduce a novel "Real-Sim-Real" framework that automatically simulates physics-based sensor attack vectors, including six attacks targeting cameras and two targeting microphones, and validates them on real robotic systems. Through large-scale evaluations across various VLA architectures and tasks under varying attack parameters, we demonstrate significant vulnerabilities, with susceptibility patterns that reveal critical dependencies on task types and model designs. We further develop an adversarial-training-based defense that enhances VLA robustness against out-of-distribution physical perturbations caused by sensor attacks while preserving model performance. Our findings expose an urgent need for standardized robustness benchmarks and mitigation strategies to secure VLA deployments in safety-critical environments.
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
- In this paper, we investigate the possibility of cross-modality signal injection attacks, i.e., injecting
intentional electromagnetic interference (IEMI) to manipulate LiDAR output. Our insight is that the internal modules of a LiDAR, i.e., the laser receiving circuit, the monitoring sensors, and the beam-steering modules, even with strict electromagnetic compatibility (EMC) testing, can still couple with the IEMI attack signals and result in the malfunction of LiDAR systems. Based on the above attack surfaces, we propose the PhantomLiDAR attack, which manipulates LiDAR output in terms of Points Interference, Points Injection, Points Removal, and even LiDAR Power-Off. We evaluate and demonstrate the effectiveness of PhantomLiDAR with both simulated and real-world experiments on five COTS LiDAR systems. We also conduct feasibility experiments in real-world moving scenarios. We provide potential defense measures that can be implemented at both the sensor level and the vehicle system level to mitigate the risks associated with IEMI attacks.
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
