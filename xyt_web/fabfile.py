#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
from fabric.api import env, run, put, roles

#部署位置
deploy_root_dir = '/mnt/www2'
deploy_web_dir = '%s/support-finance-tools' % deploy_root_dir
# deploy_lib_dir = '%s/yr_hsh' % deploy_root_dir
# deploy_base_dir = '%s/yr_base' % deploy_root_dir
# deploy_conf_dir = '%s/yr_global' % deploy_root_dir
# deploy_yklib2_dir = '%s/yklib2' % deploy_root_dir
# deploy_thrift_dir = '%s/yr_thirdparty' % deploy_root_dir
#
# deploy_www_admin_dir = '%s/www_admin' % deploy_root_dir
# deploy_www_base_dir = '%s/www_base' % deploy_root_dir
# deploy_www_hsh_fxs_dir = '%s/www_hsh_fxs' % deploy_root_dir
# deploy_www_hsh_hys_app_dir = '%s/www_hsh_hys_app' % deploy_root_dir
# deploy_yr_admin_dir = '%s/yr_admin' % deploy_root_dir
# deploy_yr_doctors_dir = '%s/yr_doctors' % deploy_root_dir
# deploy_yr_hsh_weixin_dir = '%s/yr_hsh_weixin' % deploy_root_dir
# deploy_www_hsh_weixin_dir = '%s/www_hsh_weixin' % deploy_root_dir

env.roledefs = {
    'test': ['root@192.168.123.143'],
    # 'demo': ['root@121.42.146.230'],
    #'prod1': ['root@121.42.50.138'],
    #'prod2': ['root@115.29.35.57'],
}

env.password = '1234567'
# env.password = 'Xa953N3Lopq4m0b'
#env.password = 'Qafuy75cv'
#env.password = 'Xaz91pC37Yag'


@roles('test')
def deploy():
    # service stop
    # run('service nginx stop')
    # run('service supervisord stop')

    # 清除文件夹
    run('rm -rf %s' % deploy_web_dir)
    # run('rm -rf %s' % deploy_lib_dir)
    # run('rm -rf %s' % deploy_base_dir)
    # run('rm -rf %s' % deploy_conf_dir)
    # run('rm -rf %s' % deploy_yklib2_dir)
    # run('rm -rf %s' % deploy_thrift_dir)


    # run('rm -rf %s' % deploy_www_admin_dir)
    # run('rm -rf %s' % deploy_www_base_dir)
    # run('rm -rf %s' % deploy_www_hsh_fxs_dir)
    # run('rm -rf %s' % deploy_www_hsh_hys_app_dir)
    # run('rm -rf %s' % deploy_yr_admin_dir)
    # run('rm -rf %s' % deploy_yr_doctors_dir)
    # run('rm -rf %s' % deploy_yr_hsh_weixin_dir)
    # run('rm -rf %s' % deploy_www_hsh_weixin_dir)

    # 创建远程文件夹
    run('test -d %s || mkdir -p %s' % (deploy_web_dir, deploy_web_dir))
    # run('test -d %s || mkdir %s' % (deploy_lib_dir, deploy_lib_dir))
    # run('test -d %s || mkdir %s' % (deploy_base_dir, deploy_base_dir))
    # run('test -d %s || mkdir %s' % (deploy_conf_dir, deploy_conf_dir))
    # run('test -d %s || mkdir %s' % (deploy_yklib2_dir, deploy_yklib2_dir))
    # run('test -d %s || mkdir %s' % (deploy_thrift_dir, deploy_thrift_dir))

    # run('test -d %s || mkdir %s' % (deploy_www_admin_dir, deploy_www_admin_dir))
    # run('test -d %s || mkdir %s' % (deploy_www_base_dir, deploy_www_base_dir))
    # run('test -d %s || mkdir %s' % (deploy_www_hsh_fxs_dir, deploy_www_hsh_fxs_dir))
    # run('test -d %s || mkdir %s' % (deploy_www_hsh_hys_app_dir, deploy_www_hsh_hys_app_dir))
    # run('test -d %s || mkdir %s' % (deploy_yr_admin_dir, deploy_yr_admin_dir))
    # run('test -d %s || mkdir %s' % (deploy_yr_doctors_dir, deploy_yr_doctors_dir))
    # run('test -d %s || mkdir %s' % (deploy_yr_hsh_weixin_dir, deploy_yr_hsh_weixin_dir))
    # run('test -d %s || mkdir %s' % (deploy_www_hsh_weixin_dir, deploy_www_hsh_weixin_dir))

    # 拷贝文件
    put('../*', '%s' % deploy_web_dir)
    # put('../yr_hsh/*', '%s' % deploy_lib_dir)
    # put('../yr_base/*', '%s' % deploy_base_dir)
    # put('../yr_global/*', '%s' % deploy_conf_dir)
    # put('../../yklib2/*', '%s' % deploy_yklib2_dir)
    # put('../yr_thirdparty/*', '%s' % deploy_thrift_dir)

    # put('../www_admin/*', '%s' % deploy_www_admin_dir)
    # put('../www_base/*', '%s' % deploy_www_base_dir)
    # put('../www_hsh_fxs/*', '%s' % deploy_www_hsh_fxs_dir)
    # put('../www_hsh_hys_app/*', '%s' % deploy_www_hsh_hys_app_dir)
    # put('../yr_admin/*', '%s' % deploy_yr_admin_dir)
    # put('../yr_doctors/*', '%s' % deploy_yr_doctors_dir)
    # put('../yr_hsh_weixin/*', '%s' % deploy_yr_hsh_weixin_dir)
    # put('../www_hsh_weixin/*', '%s' % deploy_www_hsh_weixin_dir)

    # service start
    # run('service supervisord start')
    # run('service nginx start')