#!/usr/bin/env python
from gomatic import *

configurator = GoCdConfigurator(HostRestClient("localhost:8153", ssl=False))
pipeline = configurator\
	.ensure_pipeline_group("createdGroup")\
	.ensure_replacement_of_pipeline("CreatedByAnotherPipeline")\
	.set_git_url("https://github.com/renatalourena/dojo_scala_fisl_17.git")
stage = pipeline.ensure_stage("createdStage")
job = stage.ensure_job("createdJob")
job.add_task(ExecTask(['pwd']))

configurator.save_updated_config()
