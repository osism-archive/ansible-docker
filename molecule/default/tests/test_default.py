import pytest


@pytest.fixture()
def AnsibleDefaults(host):
    return host.ansible("include_vars", "defaults.yml")["ansible_facts"]


def test_apt_preferences_docker_compose_file(host):
    f = host.file("/etc/apt/preferences.d/docker-compose")
    assert f.exists
    assert f.is_file


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


def test_docker_socket_tcp(host):
    s = host.socket("tcp://127.0.0.1:2375")
    assert s.is_listening


def test_docker_user_group(host, AnsibleDefaults):
    user = host.user(AnsibleDefaults["docker_user"])
    assert user.name == AnsibleDefaults["docker_user"]
    assert user.group == AnsibleDefaults["docker_user"]
    assert "docker" in user.groups
