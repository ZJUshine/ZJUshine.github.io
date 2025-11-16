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

I graduated from EE College, Zhejiang University (浙江大学电气学院) with a bachelor’s degree and now studying for PhD in <a href="http://usslab.org">USSLAB</a>

My research interest includes security of voice and automatic drive. I have published 4 paper at the CCF-A conferences with total <a href='https://scholar.google.com/citations?user=cz6jVd0AAAAJ'>google scholar citations <strong><span id='total_cit'>7+</span></strong></a> (<a href='https://scholar.google.com/citations?user=cz6jVd0AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).

# 🔥 News
- *2023.09*: &nbsp;🎉🎉 NDSS 2024, Inaudible Adversarial Perturbation: Manipulating the Recognition of User Speech in Real Time. 
- *2024.01*: &nbsp;🎉🎉 WWW 2024, Unity is Strength? Benchmarking the Robustness of Fusion-based 3D Object Detection against Physical Sensor Attack.
- *2024.09*: &nbsp;🎉🎉 NDSS 2025, PhantomLiDAR: Cross-modality Signal Injection Attacks against LiDAR.
- *2025.11*: &nbsp;🎉🎉 AAAI 2026, Phantom Menace: Exploring and Enhancing the Robustness of VLA Models against Physical Sensor Attacks.

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NDSS 2024</div><img src='images/IAP-500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Inaudible Adversarial Perturbation: Manipulating the Recognition of User Speech in Real Time](https://arxiv.org/abs/2308.01040)

Xinfeng Li, Chen Yan, **Xuancun Lu**, Zihan Zeng, Xiaoyu Ji, Wenyuan Xu

[**Project**]() <strong><span class='show_paper_citations' data='cz6jVd0AAAAJ:u5HHmVD_uO8C'></span></strong>
- We propose VRIFLE, an inaudible adversarial perturbation (IAP) attack via ultrasound delivery that can manipulate ASRs as a user speaks. 
- Github https://github.com/LetterLiGo/Adversarial_Audio_Attack-VRifle
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WWW 2024</div><img src='images/PSA-Fusion.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Unity is Strength? Benchmarking the Robustness of Fusion-based 3D Object Detection against Physical Sensor Attack]()

Zizhi Jin, **Xuancun Lu**, Bo Yang,Yushi Chen, Chen Yan, Xiaoyu Ji, Wenyuan Xu

[**Project**]() <strong><span class='show_paper_citations' data='cz6jVd0AAAAJ:u-x6o8ySG0sC'></span></strong>
- Our new benchmark features 5 types of LiDAR attacks and 6 types of camera attacks. Different from traditional benchmarks, we take the physical sensor attacks into consideration during the corruption construction. Then, we systematically investigate 7 MSF-based and 5 single-modality 3D object detection models with different fusion architectures.
- Homepage https://zjushine.github.io/PSA-Fusion/
- Github https://github.com/Jinzizhisir/PSA-Fusion/
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NDSS 2025</div><img src='images/PhantomLiDAR.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PhantomLiDAR: Cross-modality Signal Injection Attacks against LiDAR]()

Zizhi Jin, Qinhong Jiang, **Xuancun Lu**, Chen Yan, Xiaoyu Ji, Wenyuan Xu

[**Project**]() <strong><span class='show_paper_citations' data='cz6jVd0AAAAJ:d1gkVwhDpl0C'></span></strong>
- In this paper, we investigate the possibility of cross-modality signal injection attacks, i.e., injecting
intentional electromagnetic interference (IEMI) to manipulate LiDAR output. Our insight is that the internal modules of a LiDAR, i.e., the laser receiving circuit, the monitoring sensors, and the beam-steering modules, even with strict electromagnetic compatibility (EMC) testing, can still couple with the IEMI attack signals and result in the malfunction of LiDAR systems. Based on the above attack surfaces, we propose the PhantomLiDAR attack, which manipulates LiDAR output in terms of Points Interference, Points Injection, Points Removal, and even LiDAR Power-Off. We evaluate and demonstrate the effectiveness of PhantomLiDAR with both simulated and real-world experiments on five COTS LiDAR systems. We also conduct feasibility experiments in real-world moving scenarios. We provide potential defense measures that can be implemented at both the sensor level and the vehicle system level to mitigate the risks associated with IEMI attacks.
- Homepage https://sites.google.com/view/phantomlidar
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='images/PhantomMenace.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Phantom Menace: Exploring and Enhancing the Robustness of VLA Models against Physical Sensor Attacks]()

**Xuancun Lu**, Jiaxiang Chen, Shilin Xiao, Zizhi Jin, Zhangrui Chen, Hanwen Yu, Bohan Qian, Ruochen Zhou, Xiaoyu Ji, Wenyuan Xu

[**Project**]() <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Vision-Language-Action (VLA) models revolutionize robotic systems by enabling end-to-end perception-to-action pipelines that integrate multiple sensory modalities, such as visual signals processed by cameras and auditory signals captured by microphones. This multi-modality integration allows VLA models to interpret complex, real-world environments using diverse sensor data streams. Given the fact that VLA-based systems heavily rely on the sensory input, the security of VLA models against physical-world sensor attacks remains critically underexplored. To address this gap, we present the first systematic study of physical sensor attacks against VLAs, quantifying the influence of sensor attacks and investigating the defenses for VLA models. We introduce a novel "Real-Sim-Real" framework that automatically simulates physics-based sensor attack vectors, including six attacks targeting cameras and two targeting microphones, and validates them on real robotic systems. Through large-scale evaluations across various VLA architectures and tasks under varying attack parameters, we demonstrate significant vulnerabilities, with susceptibility patterns that reveal critical dependencies on task types and model designs. We further develop an adversarial-training-based defense that enhances VLA robustness against out-of-distribution physical perturbations caused by sensor attacks while preserving model performance. Our findings expose an urgent need for standardized robustness benchmarks and mitigation strategies to secure VLA deployments in safety-critical environments.
- Code https://github.com/ZJUshine/Phantom-Menace
</div>
</div>


# 📖 Educations
- *2023.06 - now*, PhD, USSLAB, EE College, Zhejiang Univeristy, Hangzhou.
- *2019.09 - 2023.06*, Undergraduate, EE College, Zhejiang Univeristy, Hangzhou.



# 🎖 Honors and Awards
<!-- - *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->
# 💬 Invited Talks
<!-- - *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->
<!-- - *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 💻 Internships
<!-- - *2019.05 - 2020.02*, [Lorem](https://github.com/), China. -->
