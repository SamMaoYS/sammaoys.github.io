Yongsen Mao
###########


:save_as: index.html
:url:
:description: I'm a thesis-based master student at SFU (Simon Fraser University), specializing in the fields of 3D Computer Vision and Graphics.
:summary: I'm a thesis-based master student at SFU (Simon Fraser University), specializing in the fields of 3D Computer Vision and Graphics.
:hide_navbar_brand: False
:landing:
    .. container:: m-container

        .. container:: m-row

            .. container:: m-col-l-6

                .. image:: {static}/images/yongsen_avatar.jpg
                    :alt: Yongsen Mao
                    :width: 50%

            .. container:: m-col-l-6

                .. raw:: html

                    <h1 style="text-transform: capitalize;">Yongsen Mao</h1>

                    <div>I'm a thesis-based master student at <a href="https://www.sfu.ca" class="m-link-wrap">SFU</a> (Simon Fraser University), specializing in the fields of 3D Computer Vision and Graphics. I am fortunate to be supervised by Professors <a href="https://msavva.github.io" class="m-link-wrap">Manolis Savva</a> and mentored by <a href="https://angelxuanchang.github.io" class="m-link-wrap">Angel Xuan Chang</a> in the <a href="https://gruvi.cs.sfu.ca" class="m-link-wrap">GrUVi Lab</a>. My primary interest lies in the generation and understanding of 3D scenes for downstream vision and robotics applications. Prior to this, I received B.Eng. from <a href="https://www.zju.edu.cn/english" class="m-link-wrap">ZJU</a> (Zhejiang University) and SFU.</div>

                    <br/>
                    <br/>
                    
                    <div>
                    sam_mao-{at}-sfu-[dot]-ca&emsp;
                    <a href="https://scholar.google.com/citations?user=bm9JqwMAAAAJ&hl=en" class="m-link-wrap">Google Scholar</a>&emsp;
                    <a href="https://github.com/SamMaoYS" class="m-link-wrap">GitHub</a>
                    </div>



News
----


Publications
------------

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

                    <div class="m-text">arXiv</div>

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

            

