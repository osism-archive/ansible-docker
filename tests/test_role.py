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


def test_docker_engine_is_installed(Package):
    package = Package("docker-engine")
    assert package.is_installed


def test_linux_image_extra_is_installed(Package):
    package = Package("linux-image-extra-virtual")
    assert package.is_installed


def test_python_docker_is_installed(Package):
    package = Package("python-docker")
    assert package.is_installed


def test_docker_serivce_running_and_enabled(Service):
    service = Service("docker.service")
    assert service.is_running
    assert service.is_enabled


def test_docker_socket_running_and_enabled(Service):
    service = Service("docker.socket")
    assert service.is_running
    assert service.is_enabled


def test_docker_socket_is_listening(Socket):
    socket = Socket("unix:///var/run/docker.sock")
    assert socket.is_listening


def test_systemd_docker_overlay_file_exists(File):
    file = File("/etc/systemd/system/docker.service.d/overlay.conf")
    assert file.exists
    assert file.is_file


def test_docker_limits_file_exists(File):
    file = File("/etc/security/limits.d/docker.conf")
    assert file.exists
    assert file.is_file
