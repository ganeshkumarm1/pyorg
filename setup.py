# -*- coding: utf-8 -*-
# @Author: GaNeShKuMaRm
# @Date:   2017-05-14 19:15:41
# @Last Modified by:   GaNeShKuMaRm
# @Last Modified time: 2017-05-14 19:46:48


from setuptools import setup

setup(
        name="pyorg",
        version="0.0.1",
        description="Organize files based on their extenstion",
        url="",
        author="Ganesh Kumar M",
        author_email="ganeshkumar.m1996@gmail.com",
        license='MIT',
        packages=["pyorg"],
        entry_points={
             'console_scripts':[
             'pyorg = pyorg.pyorg:main'
             ]
        },
        zip_safe=False
)
