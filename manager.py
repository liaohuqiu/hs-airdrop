#!/usr/bin/env python

import os

from cpbox.app import devops
from cpbox.tool import dockerutil
from cpbox.tool import functocli

APP_NAME = 'hs'
image_name = 'liaohuqiu/hs-airdrop:2.0'


class App(devops.DevOpsApp):

    def __init__(self, **kwargs):
        devops.DevOpsApp.__init__(self, APP_NAME, log_level='debug', **kwargs)

    def build_image(self, push=False):
        cmd = 'docker build -t %s %s/docker/' % (image_name, self.root_dir)
        self.shell_run(cmd)
        if push:
            cmd = 'docker push %s' % (image_name)
        self.shell_run(cmd)

    def run(self, key_file, args):
        key_file = os.path.expanduser(key_file)
        key_file = os.path.abspath(key_file)
        working_dir = '/opt/app'
        volumes = {
            key_file: key_file,
        }
        container_name = 'fs'
        cmd = '%s/hs-airdrop/bin/hs-airdrop %s %s' % (working_dir, key_file, args)
        docker_args = dockerutil.base_docker_args(container_name=container_name, volumes=volumes,
                                           auto_hostname=False)
        docker_args += ' -w %s' % (working_dir)

        self.stop_container(container_name)
        image = 'docker-genesis.0xhash.cn' + image_name
        cmd = 'docker run -it %s --rm %s %s' % (docker_args, image, cmd)
        self.shell_run(cmd)


if __name__ == '__main__':
    common_args_option = {}
    functocli.run_app(App, common_args_option=common_args_option)
