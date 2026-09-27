Yongsen Mao
###########


:save_as: index.html
:url:
:description: I graduated as a thesis-based master student at SFU (Simon Fraser University), specializing in the fields of 3D Computer Vision and Graphics.
:summary: I graduated as a thesis-based master student at SFU (Simon Fraser University), specializing in the fields of 3D Computer Vision and Graphics.
:hide_navbar_brand: False
:landing:
    .. container:: m-container

        .. container:: m-row

            .. container:: m-col-l-6

                .. image:: {static}/images/profile.jpg
                    :alt: Yongsen Mao
                    :width: 70%

            .. container:: m-col-l-6

                .. raw:: html

                    <h1 style="text-transform: capitalize;">Yongsen Mao</h1>

                    <div>I am a Ph.D. student at <a href="https://hkust.edu.hk/">HKUST</a> in the <a href="https://github.com/IGL-HKUST" class="m-link-wrap">Intelligent Graphics Lab</a> since February 2026, supervised by Prof. <a href="https://liuyuan-pal.github.io" class="m-link-wrap">Yuan Liu</a>. I received my thesis-based M.Sc. from <a href="https://www.sfu.ca" class="m-link-wrap">Simon Fraser University</a>(SFU), supervised by Prof. <a href="https://msavva.github.io" class="m-link-wrap">Manolis Savva</a> and mentored by Prof. <a href="https://angelxuanchang.github.io" class="m-link-wrap">Angel Xuan Chang</a> in the <a href="https://gruvi.cs.sfu.ca" class="m-link-wrap">GrUVi Lab</a>. I earned my B.Eng. from <a href="https://www.zju.edu.cn/english" class="m-link-wrap">Zhejiang University</a>(ZJU) and SFU. I also worked as a full-time Research Engineer at <a href="https://www.manycoretech.com/" class="m-link-wrap">ManycoreTech</a>.<br>My research focuses on the generation and understanding of the world for downstream vision and robotics applications.</div>


                    <br/>
                    <br/>
                    
                    <div>
                    sammaoys-{at}-outlook-[dot]-com&emsp;
                    <a href="https://scholar.google.com/citations?user=bm9JqwMAAAAJ&hl=en" class="m-link-wrap">Google Scholar</a>&emsp;
                    <a href="https://github.com/SamMaoYS" class="m-link-wrap">GitHub</a>
                    </div>



News
--------------
.. container:: m-container

    .. container:: m-row

        .. raw:: html
            
            <div>
                <p>2026/09 Our paper NaLA is accepted to ECCV 2026.</p>
                <p>2026/07 Our paper ReVSI is accepted to ICML 2026.</p>
                <p>2026/03 Our paper SpatialGen is accepted to 3DV 2026.</p>
                <p>2025/12 We released the KlingAvatar 2.0 technical report.</p>
                <p>2025/09 Our paper SpatialLM is accepted to NeurIPS 2025.</p>
                
                <details>
                    <summary class="m-text m-dim" style="list-style: none; cursor: pointer; font-weight: normal; margin-bottom: 10px;"><p>More...</p></summary>
                    <div style="margin-left: 0; padding: 8px 0;">
                        <p>2025/06 We released <a href="https://huggingface.co/manycore-research/SpatialLM1.1-Qwen-0.5B">SpatialLM 1.1</a>, an improved version of SpatialLM.</p>
                        <p>2025/03 We started a new open-source project: <a href="https://manycore-research.github.io/SpatialLM">SpatialLM</a>.</p>
                        <p>2024/06 Our layout controlnet model released on huggingface <a href="https://huggingface.co/kujiale-ai/controlnet-layout">kujiale-ai/controlnet-layout</a>.</p>
                        <p>2024/05 Our papers HSSD-200 and Ego-Exo4D are accepted to CVPR 2024.</p>
                        <p>2023/11 Joined <a href="https://www.kujiale.com/">KuJiaLe</a>/<a href="https://www.coohom.com"> Coohom </a> as a research engineer.</p>
                    </div>
                </details>
            </div>

Publications
------------

.. container:: m-row m-block m-primary

            .. container:: m-col-l-4

                .. image:: {static}/images/papers/nala.jpg
                    :alt: nala

            .. container:: m-col-l-8

                .. raw:: html
                    
                    <h3>NaLA: A 3D Native LLM Layout Agent for High-quality 3D Scene Generation</h3>

                    <div class="m-text">
                        <a>Cheng Wan</a>, Yongsen Mao, <a>Wenzheng Wu</a>, <a>Yuxuan Xie</a>, <a href="https://xccelephant.github.io/" class="m-link-wrap">Chucheng Xiang</a>, <a href="https://rainzor.github.io/" class="m-link-wrap">Runze Wang</a>, <a>Xiang Zhang</a>, <a>Zhongyuan Liu</a>, <a href="https://facultyprofiles.hkust-gz.edu.cn/faculty-personal-page?id=626" class="m-link-wrap">Rushi Dai</a>, <a href="https://liuyuan-pal.github.io" class="m-link-wrap">Yuan Liu</a>
                    </div>
                    <br/>

                    <div class="m-text">
                    Recently, Large Language Models (LLMs) have emerged as promising layout agents for 3D scene generation. Existing layout agents still suffer from implausible layout generation because most of them convert 3D assets and 3D layouts into textual descriptions as inputs and outputs, which involves severe information loss due to the modality gap between texts and 3D assets and 3D layouts. We propose NaLA, a native 3D LLM layout agent for high-quality 3D scene generation by placing 3D assets in the scene. For the inputs, NaLA encodes 3D scene boundaries and 3D assets directly into the LLM, preserving fine-grained geometry and enabling explicit reasoning over relationships like collisions, surface supporting, and containment. To accurately output the positions and orientations of assets, NaLA adopts a coarse-to-fine prediction mechanism that first predicts discrete poses in an autoregressive manner and then refines the discrete poses with a continuous regression. Trained on diverse layout datasets, NaLA attains strong geometric perception and layout coherence. Experiments demonstrate that NaLA outperforms prior layout agents in both generation quality and inference efficiency, with comprehensive ablation studies to verify each component's effectiveness.
                    </div>

                    <br/>

                    <div class="m-text">ECCV 2026</div>

                    <div class="m-text">
                    <a href="https://arxiv.org/abs/2606.29395" class="m-link-wrap">Paper</a>, <a href="https://adamcwan.github.io/NaLA/" class="m-link-wrap">Project</a>, <a href="https://github.com/adamcwan/NaLA-code" class="m-link-wrap">Code</a>
                    </div>

.. container:: m-row m-block m-primary

            .. container:: m-col-l-4

                .. image:: {static}/images/papers/revsi.jpg
                    :alt: revsi

            .. container:: m-col-l-8

                .. raw:: html
                    
                    <h3>ReVSI: Rebuilding Visual Spatial Intelligence Evaluation for Accurate Assessment of VLM 3D Reasoning</h3>

                    <div class="m-text">
                        <a href="https://github.com/eamonn-zh/" class="m-link-wrap">Yiming Zhang</a>*, <a href="https://jcchen.me/" class="m-link-wrap">Jiacheng Chen</a>*, <a href="https://christinatan0704.github.io/mysite/" class="m-link-wrap">Jiaqi Tan</a>, Yongsen Mao, <a href="https://wenhuchen.github.io/" class="m-link-wrap">Wenhu Chen</a>, <a href="https://angelxuanchang.github.io/" class="m-link-wrap">Angel X. Chang</a>
                    </div>
                    <br/>

                    <div class="m-text">
                    Current evaluations of spatial intelligence can be systematically invalid under modern vision-language model (VLM) settings. First, many benchmarks derive question-answer (QA) pairs from point-cloud-based 3D annotations originally curated for traditional 3D perception. When such annotations are treated as ground truth for video-based evaluation, reconstruction and annotation artifacts can miss objects that are clearly visible in the video, mislabel object identities, or corrupt geometry-dependent answers (e.g., size), yielding incorrect or ambiguous QA pairs. Second, evaluations often assume full-scene access, while many VLMs operate on sparsely sampled frames (e.g., 16-64), making many questions effectively unanswerable under the actual model inputs. We improve evaluation validity by introducing ReVSI, a benchmark and protocol that ensures each QA pair is answerable and correct under the model's actual inputs. To this end, we re-annotate objects and geometry across 381 scenes from 5 datasets to improve data quality, and regenerate all QA pairs with rigorous bias mitigation and human verification using professional 3D annotation tools. We further enhance evaluation controllability by providing variants across multiple frame budgets (16/32/64/all) and fine-grained object visibility metadata, enabling controlled diagnostic analyses. Evaluations of general and domain-specific VLMs on ReVSI reveal systematic failure modes that are obscured by prior benchmarks, yielding a more reliable and diagnostic assessment of spatial intelligence.
                    </div>

                    <br/>

                    <div class="m-text">ICML 2026</div>

                    <div class="m-text">
                    <a href="https://arxiv.org/abs/2604.24300" class="m-link-wrap">Paper</a>, <a href="https://3dlg-hcvc.github.io/revsi/" class="m-link-wrap">Project</a>, <a href="https://github.com/3dlg-hcvc/revsi" class="m-link-wrap">Code</a>
                    </div>

.. container:: m-row m-block m-primary

            .. container:: m-col-l-4

                .. image:: {static}/images/papers/spatialgen.jpg
                    :alt: spatialgen

            .. container:: m-col-l-8

                .. raw:: html
                    
                    <h3>SpatialGen: Layout-guided 3D Indoor Scene Generation</h3>

                    <div class="m-text">
                        <a href="https://fangchuan.github.io/" class="m-link-wrap">Chuan Fang</a>, <a href="https://hengli.me/" class="m-link-wrap">Heng Li</a>, <a href="https://yixunliang.github.io/" class="m-link-wrap">Yixun Liang</a>, <a href="https://bertjiazheng.github.io" class="m-link-wrap">Jia Zheng</a>, Yongsen Mao, <a href="https://liuyuan-pal.github.io" class="m-link-wrap">Yuan Liu</a>, <a href="https://scholar.google.com/citations?user=dwvfKSkAAAAJ" class="m-link-wrap">Rui Tang</a>, <a href="https://zihan-z.github.io/" class="m-link-wrap">Zihan Zhou</a>, <a href="https://pingtan.people.ust.hk/index.html" class="m-link-wrap">Ping Tan</a>
                    </div>
                    <br/>

                    <div class="m-text">
                    Creating high-fidelity 3D models of indoor environments is essential for applications in design, virtual reality, and robotics. However, manual 3D modeling remains time-consuming and labor-intensive. While recent advances in generative AI have enabled automated scene synthesis, existing methods often face challenges in balancing visual quality, diversity, semantic consistency, and user control. A major bottleneck is the lack of a large-scale, high-quality dataset tailored to this task. To address this gap, we introduce a comprehensive synthetic dataset, featuring 12,328 structured annotated scenes with 57,431 rooms, and 4.7M photorealistic 2D renderings. Leveraging this dataset, we present SpatialGen, a novel multi-view multi-modal diffusion model that generates realistic and semantically consistent 3D indoor scenes. Given a 3D layout and a reference image (derived from a text prompt), our model synthesizes appearance (color image), geometry (scene coordinate map), and semantic (semantic segmentation map) from arbitrary viewpoints, while preserving spatial consistency across modalities. SpatialGen consistently generates superior results to previous methods in our experiments. We are open-sourcing our data and models to empower the community and advance the field of indoor scene understanding and generation.
                    </div>

                    <br/>

                    <div class="m-text">3DV 2026</div>

                    <div class="m-text">
                    <a href="https://arxiv.org/abs/2509.14981" class="m-link-wrap">Paper</a>, <a href="https://manycore-research.github.io/SpatialGen/" class="m-link-wrap">Project</a>, <a href="https://github.com/manycore-research/SpatialGen" class="m-link-wrap">Code</a>
                    </div>

.. container:: m-row m-block m-primary

            .. container:: m-col-l-4

                .. image:: {static}/images/papers/klingavatar.jpg
                    :alt: klingavatar

            .. container:: m-col-l-8

                .. raw:: html
                    
                    <h3>KlingAvatar 2.0 Technical Report</h3>

                    <div class="m-text">
                        <a>Jialu Chen, Yikang Ding, Zhixue Fang, Kun Gai, Yuan Gao, Kang He, Jingyun Hua, Boyuan Jiang, Mingming Lao, Xiaohan Li, Hui Liu, Jiwen Liu, Xiaoqiang Liu*, </a><a href="https://liuyuan-pal.github.io" class="m-link-wrap">Yuan Liu</a><a>, Shun Lu,</a> Yongsen Mao<a>, Yingchao Shao, Huafeng Shi, Xiaoyu Shi, Peiqin Sun, Songlin Tang, Pengfei Wan, Chao Wang, Xuebo Wang, Haoxian Zhang, Yuanxing Zhang, Yan Zhou</a>
                    </div>
                    <br/>

                    <div class="m-text">
                    Avatar video generation models have achieved remarkable progress in recent years. However, prior work exhibits limited efficiency in generating long-duration high-resolution videos, suffering from temporal drifting, quality degradation, and weak prompt following as video length increases. To address these challenges, we propose KlingAvatar 2.0, a spatio-temporal cascade framework that performs upscaling in both spatial resolution and temporal dimension. The framework first generates low-resolution blueprint video keyframes that capture global semantics and motion, and then refines them into high-resolution, temporally coherent sub-clips using a first-last frame strategy, while retaining smooth temporal transitions in long-form videos. To enhance cross-modal instruction fusion and alignment in extended videos, we introduce a Co-Reasoning Director composed of three modality-specific large language model (LLM) experts. These experts reason about modality priorities and infer underlying user intent, converting inputs into detailed storylines through multi-turn dialogue. A Negative Director further refines negative prompts to improve instruction alignment. Building on these components, we extend the framework to support ID-specific multi-character control. Extensive experiments demonstrate that our model effectively addresses the challenges of efficient, multimodally aligned long-form high-resolution video generation, delivering enhanced visual clarity, realistic lip-teeth rendering with accurate lip synchronization, strong identity preservation, and coherent multimodal instruction following.
                    </div>

                    <br/>

                    <div class="m-text">Technical Report, 2025</div>

                    <div class="m-text">
                    <a href="https://arxiv.org/abs/2512.13313" class="m-link-wrap">Paper</a>, <a href="https://app.klingai.com/global/ai-human/image/new/" class="m-link-wrap">Project</a>
                    </div>

.. container:: m-row m-block m-primary

            .. container:: m-col-l-4

                .. image:: {static}/images/papers/spatiallm.jpg
                    :alt: spatiallm

            .. container:: m-col-l-8

                .. raw:: html
                    
                    <h3>SpatialLM: Training Large Language Models for Structured Indoor Modeling</h3>

                    <div class="m-text">
                        Yongsen Mao*, <a>Junhao Zhong</a>*, <a href="https://fangchuan.github.io/">Chuan Fang</a>, <a href="https://bertjiazheng.github.io">Jia Zheng</a>, <a>Rui Tang</a>, <a>Hao Zhu</a>, <a href="https://pingtan.people.ust.hk/index.html">Ping Tan</a>, <a href="https://zihan-z.github.io/">Zihan Zhou</a>
                    </div>
                    <br/>

                    <div class="m-text">
                    SpatialLM is a large language model designed to process 3D point cloud data and generate structured 3D scene understanding outputs. These outputs include architectural elements like walls, doors, windows, and oriented object boxes with their semantic categories. Unlike previous methods which exploit task-specific network designs, our model adheres to the standard multimodal LLM architecture and is fine-tuned directly from open-source LLMs. To train SpatialLM, we collect a large-scale, high-quality synthetic dataset consisting of the point clouds of 12,328 indoor scenes (54,778 rooms) with ground-truth 3D annotations, and conduct a careful study on various modeling and training decisions. On public benchmarks, our model gives state-of-the-art performance in layout estimation and competitive results in 3D object detection. With that, we show a feasible path for enhancing the spatial understanding capabilities of modern LLMs for applications in augmented reality, embodied robotics, and more.
                    </div>

                    <br/>

                    <div class="m-text">NeurIPS 2025</div>

                    <div class="m-text">
                    <a href="https://arxiv.org/abs/2506.07491" class="m-link-wrap">Paper</a>, <a href="https://manycore-research.github.io/SpatialLM/" class="m-link-wrap">Project</a>, <a href="https://github.com/manycore-research/SpatialLM" class="m-link-wrap">Code</a>
                    </div>

.. container:: m-row m-block m-primary

            .. container:: m-col-l-4

                .. image:: {static}/images/papers/egoexo4d.jpeg
                    :alt: egoexo4d

            .. container:: m-col-l-8

                .. raw:: html
                    
                    <h3>Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives</h3>

                    <div class="m-text">
                    <a>Kristen Grauman, Andrew Westbury, Lorenzo Torresani, Kris Kitani, Jitendra Malik, Triantafyllos Afouras, Kumar Ashutosh, Vijay Baiyya, Siddhant Bansal, Bikram Boote, Eugene Byrne, Zach Chavis, Joya Chen, Feng Cheng, Fu-Jen Chu, Sean Crane, Avijit Dasgupta, Jing Dong, Maria Escobar, Cristhian Forigua, Abrham Gebreselasie, Sanjay Haresh, Jing Huang, Md Mohaiminul Islam, Suyog Jain, Rawal Khirodkar, Devansh Kukreja, Kevin J Liang, Jia-Wei Liu, Sagnik Majumder,</a> Yongsen Mao <a>, Miguel Martin, Effrosyni Mavroudi, Tushar Nagarajan, Francesco Ragusa, Santhosh Kumar Ramakrishnan, Luigi Seminara, Arjun Somayazulu, Yale Song, Shan Su, Zihui Xue, Edward Zhang, Jinxu Zhang, Angela Castillo, Changan Chen, Xinzhu Fu, Ryosuke Furuta, Cristina Gonzalez, Prince Gupta, Jiabo Hu, Yifei Huang, Yiming Huang, Weslie Khoo, Anush Kumar, Robert Kuo, Sach Lakhavani, Miao Liu, Mi Luo, Zhengyi Luo, Brighid Meredith, Austin Miller, Oluwatumininu Oguntola, Xiaqing Pan, Penny Peng, Shraman Pramanick, Merey Ramazanova, Fiona Ryan, Wei Shan, Kiran Somasundaram, Chenan Song, Audrey Southerland, Masatoshi Tateno, Huiyu Wang, Yuchen Wang, Takuma Yagi, Mingfei Yan, Xitong Yang, Zecheng Yu, Shengxin Cindy Zha, Chen Zhao, Ziwei Zhao, Zhifan Zhu, Jeff Zhuo, Pablo Arbelaez, Gedas Bertasius, David Crandall, Dima Damen, Jakob Engel, Giovanni Maria Farinella, Antonino Furnari, Bernard Ghanem, Judy Hoffman, C. V. Jawahar, Richard Newcombe, Hyun Soo Park, James M. Rehg, Yoichi Sato, Manolis Savva, Jianbo Shi, Mike Zheng Shou, Michael Wray</a>
                    </div>
                    <br/>

                    <div class="m-text">
                    We present Ego-Exo4D, a diverse, large-scale multimodal multiview video dataset and benchmark challenge. Ego-Exo4D centers around simultaneously-captured egocentric and exocentric video of skilled human activities (e.g., sports, music, dance, bike repair). 740 participants from 13 cities worldwide performed these activities in 123 different natural scene contexts, yielding long-form captures from 1 to 42 minutes each and 1,286 hours of video combined. The multimodal nature of the dataset is unprecedented: the video is accompanied by multichannel audio, eye gaze, 3D point clouds, camera poses, IMU, and multiple paired language descriptions -- including a novel "expert commentary" done by coaches and teachers and tailored to the skilled-activity domain. To push the frontier of first-person video understanding of skilled human activity, we also present a suite of benchmark tasks and their annotations, including fine-grained activity understanding, proficiency estimation, cross-view translation, and 3D hand/body pose. All resources are open sourced to fuel new research in the community.
                    </div>

                    <br/>

                    <div class="m-text">CVPR 2024, Oral</div>

                    <div class="m-text">
                    <a href="https://arxiv.org/abs/2311.18259" class="m-link-wrap">Paper</a>, <a href="https://ego-exo4d-data.org/" class="m-link-wrap">Project</a>, <a href="https://docs.ego-exo4d-data.org" class="m-link-wrap">Code</a>
                    </div>

.. container:: m-row m-block m-primary

            .. container:: m-col-l-4

                .. image:: {static}/images/papers/hssd.png
                    :alt: hssd

            .. container:: m-col-l-8

                .. raw:: html
                    
                    <h3>Habitat Synthetic Scenes Dataset (HSSD-200): <br/>
                     An Analysis of 3D Scene Scale and Realism Tradeoffs for ObjectGoal Navigation</h3>

                    <div class="m-text">
                    <a href="https://mukulkhanna.github.io/">Mukul Khanna</a>*, Yongsen Mao*, <a href="https://jianghanxiao.github.io/">Hanxiao Jiang</a>, <a href="https://www.sanjayharesh.com/">Sanjay Haresh</a>, <a href="https://cs.stanford.edu/~bps/">Brennan Shacklett</a>, <a href="https://faculty.cc.gatech.edu/~dbatra/">Dhruv Batra</a>, <a href="https://www.linkedin.com/in/alexander-clegg-68336839/">Alexander Clegg</a>, <a href="https://www.linkedin.com/in/ericu/">Eric Undersander</a>, <a href="https://angelxuanchang.github.io/">Angel X. Chang</a>, <a href="https://msavva.github.io/">Manolis Savva</a>
                    </div>
                    <br/>

                    <div class="m-text">
                    We contribute the Habitat Synthetic Scenes Dataset (HSSD-200), a dataset of 211 high-quality 3D scenes, and use it to test navigation agent generalization to realistic 3D environments. Our dataset represents real interiors and contains a diverse set of 18,656 models of real-world objects. We investigate the impact of synthetic 3D scene dataset scale and realism on the task of training embodied agents to find and navigate to objects (ObjectGoal navigation). By comparing to synthetic 3D scene datasets from prior work, we find that scale helps in generalization, but the benefits quickly saturate, making visual fidelity and correlation to real-world scenes more important. Our experiments show that agents trained on our smaller-scale dataset can match or outperform agents trained on much larger datasets. Surprisingly, we observe that agents trained on just 122 scenes from our dataset outperform agents trained on 10,000 scenes from the ProcTHOR-10K dataset in terms of zero-shot generalization in real-world scanned environments.
                    </div>

                    <br/>

                    <div class="m-text">CVPR 2024</div>

                    <div class="m-text">
                    <a href="https://arxiv.org/abs/2306.11290" class="m-link-wrap">Paper</a>, <a href="https://3dlg-hcvc.github.io/hssd/" class="m-link-wrap">Project</a>, <a href="https://github.com/3dlg-hcvc/hssd/" class="m-link-wrap">Code</a>
                    </div>


.. container:: m-row m-block m-primary

            .. container:: m-col-l-4

                .. image:: {static}/images/papers/multiscan.png
                    :alt: multiscan

            .. container:: m-col-l-8

                .. raw:: html
                    
                    <h3>MultiScan: Scalable RGBD scanning for 3D environments with articulated objects</h3>

                    <div class="m-text">
                        Yongsen Mao, <a href="https://github.com/eamonn-zh/">Yiming Zhang</a>, <a href="https://jianghanxiao.github.io/">Hanxiao Jiang</a>, <a href="https://angelxuanchang.github.io/">Angel X. Chang</a>, <a href="https://msavva.github.io/">Manolis Savva</a>
                    </div>

                    <br/>
                    <div class="m-text">
                        We introduce MultiScan, a scalable RGBD dataset construction pipeline leveraging commodity mobile devices to scan indoor scenes with articulated objects and web-based semantic annotation interfaces to efficiently annotate object and part semantics and part mobility parameters. We use this pipeline to collect 230 scans of 108 indoor scenes containing 9458 objects and 4331 parts. The resulting MultiScan dataset provides RGBD streams with per-frame camera poses, textured 3D surface meshes, richly annotated part-level and object-level semantic labels, and part mobility parameters. We validate our dataset on instance segmentation and part mobility estimation tasks and benchmark methods for these tasks from prior work. Our experiments show that part segmentation and mobility estimation in real 3D scenes remain challenging despite recent progress in 3D object segmentation.
                    </div>
                    <br/>

                    <div class="m-text">NeurIPS 2022</div>
                    
                    <div class="m-text">
                    <a href="https://openreview.net/pdf?id=YxUdazpgweG" class="m-link-wrap">Paper</a>, <a href="https://3dlg-hcvc.github.io/multiscan/#/" class="m-link-wrap">Project</a>, <a href="https://github.com/smartscenes/multiscan" class="m-link-wrap">Code</a>
                    </div>

.. container:: m-row m-block m-primary

            .. container:: m-col-l-4

                .. image:: {static}/images/papers/opd.png
                    :alt: opd

            .. container:: m-col-l-8

                .. raw:: html
                    
                    <h3>OPD: Single-view 3D Openable Part Detection</h3>

                    <div class="m-text">
                        <a href="https://jianghanxiao.github.io/">Hanxiao Jiang</a>, Yongsen Mao, <a href="https://msavva.github.io/">Manolis Savva</a>, <a href="https://angelxuanchang.github.io/">Angel X. Chang</a>
                    </div>

                    <br/>
                    <div class="m-text">
                        We address the task of predicting what parts of an object can open and how they move when they do so. The input is a single image of an object, and as output we detect what parts of the object can open, and the motion parameters describing the articulation of each openable part. To tackle this task, we create two datasets of 3D objects: OPDSynth based on existing synthetic objects, and OPDReal based on RGBD reconstructions of real objects. We then design OPDRCNN, a neural architecture that detects openable parts and predicts their motion parameters. Our experiments show that this is a challenging task especially when considering generalization across object categories, and the limited amount of information in a single image. Our architecture outperforms baselines and prior work especially for RGB image inputs.
                    </div>
                    <br/>

                    <div class="m-text">ECCV 2022, Oral</div>

                    <div class="m-text">
                    <a href="https://arxiv.org/pdf/2203.16421.pdf" class="m-link-wrap">Paper</a>, <a href="https://3dlg-hcvc.github.io/OPD/" class="m-link-wrap">Project</a>, <a href="https://github.com/3dlg-hcvc/OPD" class="m-link-wrap">Code</a>
                    </div>

            

