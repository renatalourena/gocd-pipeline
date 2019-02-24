#!/usr/bin/env python
from gomatic import *

configurator = GoCdConfigurator(HostRestClient("localhost:8153"))
pipeline = configurator \
    .ensure_pipeline_group("Group") \
    .ensure_replacement_of_pipeline("first_pipeline") \
    .set_git_url("http://git.url")
stage = pipeline.ensure_stage("a_stage")
job = stage.ensure_job("a_job")
job.add_task(ExecTask(['thing']))

configurator.save_updated_config()
