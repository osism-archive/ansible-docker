# Ansible betacloud.docker

![Ansible 2.2](https://img.shields.io/badge/Ansible-2.2-green.png?style=flat)
![Ansible 2.3](https://img.shields.io/badge/Ansible-2.3-green.png?style=flat)

This is an Ansible role that installs Docker on Ubuntu and CentOS servers.

Supported Linux distributions
-----------------------------

* Ubuntu 16.04 (Xenial)
* CentOS 7

Example Playbook
----------------

```yml
- hosts: all

  roles:
  - role: betacloud.docker
```

License
-------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Author information
------------------

This role was created by [Betacloud Solutions GmbH](https://betacloud-solutions.de).
