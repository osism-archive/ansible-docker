# This file is subject to the terms and conditions defined in file 'LICENSE',
# which is part of this repository.


def test_packages_are_installed(Package, SystemInfo):
    package = Package("docker-engine")
    assert package.is_installed

    if SystemInfo.distribution == 'ubuntu':
        package = Package("python-docker")
        assert package.is_installed

        package = Package("linux-image-extra-virtual")
        assert package.is_installed

    elif SystemInfo.distribution == 'centos':
        package = Package("python-docker-py")
        assert package.is_installed


def test_services_are_running_and_enabled(Service, SystemInfo):
    if SystemInfo.distribution == 'ubuntu':
        service = Service("docker.service")
        assert service.is_running
        assert service.is_enabled

        service = Service("docker.socket")
        assert service.is_running
        assert service.is_enabled

    elif SystemInfo.distribution == 'centos':
        service = Service("docker.service")
        assert service.is_running
        assert service.is_enabled


def test_socket_is_listening(Socket):
    socket = Socket("unix:///var/run/docker.sock")
    assert socket.is_listening


def test_systemd_overlay_file_exists(File):
    file = File("/etc/systemd/system/docker.service.d/overlay.conf")
    assert file.exists
    assert file.is_file


def test_limits_file_exists(File):
    file = File("/etc/security/limits.d/docker.conf")
    assert file.exists
    assert file.is_file
