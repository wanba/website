#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Snowball Beijing, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Snowball Beijing, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os.path import dirname, join
import pkutils

from setuptools import (
    find_packages,
    setup,
)

with open(join(dirname(__file__), 'shici/VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()

requirements = list(pkutils.parse_requirements('requirements.txt'))
dependencies = list(pkutils.parse_requirements('requirements.txt', True))


setup(
    name='shici',
    version=version,
    description='shici dahui',
    packages=find_packages(exclude=[]),
    author='wangzg',
    author_email='yexingren23@126.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='http://',
    install_requires=requirements,
    dependency_links=dependencies,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "shici = shici.__main__:entry_point"
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Mac',
        'Operating System :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
)
