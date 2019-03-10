#!/usr/bin/env python
from gomatic import *

configurator = GoCdConfigurator(HostRestClient("localhost:8153", ssl=False))
pipeline = configurator\
	.ensure_pipeline_group("defaultGroup")\
	.ensure_replacement_of_pipeline("FirstPipeline")\
	.set_git_material(GitMaterial("https://github.com/renatalourena/gocd-pipeline.git",
            polling=False))
stage = pipeline.ensure_stage("defaultStage")
job = stage.ensure_job("defaultJob")
job.add_task(ExecTask(['ls']))

configurator.save_updated_config()
