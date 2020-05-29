import pytest


@pytest.fixture()
def AnsibleDefaults(host):
    return host.ansible("include_vars", "defaults.yml")["ansible_facts"]


def test_apt_preferences_docker_file(host):
    f = host.file("/etc/apt/preferences.d/docker")
    assert f.exists
    assert f.is_file


def test_systemd_overlay_file(host):
    f = host.file("/etc/systemd/system/docker.service.d/overlay.conf")
    assert f.exists
    assert f.is_file


def test_docker_package(host, AnsibleDefaults):
    p = host.package(AnsibleDefaults["docker_package_name"])
    assert p.is_installed
    assert p.version.startswith(AnsibleDefaults["docker_version"])


def test_limits_file(host):
    f = host.file("/etc/security/limits.d/docker.conf")
    assert f.exists
    assert f.is_file


def test_containerd_service(host):
    f = host.service("containerd")
    assert f.is_running
    assert f.is_enabled


def test_docker_service(host):
    f = host.service("docker")
    assert f.is_running
    assert f.is_enabled


def test_docker_socket_service(host):
    f = host.service("docker.socket")
    assert f.is_running
    assert f.is_enabled


def test_docker_socket_unix(host):
    f = host.file("/var/run/docker.sock")
    assert f.exists
    assert f.is_socket


def test_docker_mountpoint(host, AnsibleDefaults):
    f = host.file("/var/lib/docker")
    assert f.exists
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o711

    m = host.mount_point("/var/lib/docker")
    assert m.exists
    assert m.filesystem == AnsibleDefaults["docker_storage_filesystem"]


def test_docker_user_group(host):
    user = host.user("ubuntu")
    assert "docker" in user.groups


def test_docker_usability(host):
    cmd = host.run("docker run -d --name testing alpine sleep infinity")
    assert cmd.succeeded

    c = host.docker("testing")
    assert c.is_running

    cmd = host.run("docker rm -f testing")
    assert cmd.succeeded

    cmd = host.run("docker rmi alpine")
    assert cmd.succeeded
