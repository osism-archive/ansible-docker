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


def test_limits_file(host):
    f = host.file("/etc/security/limits.d/docker.conf")
    assert f.exists
    assert f.is_file


def test_docker_running_and_enabled(host):
    f = host.service("docker")
    assert f.is_running
    assert f.is_enabled


def test_docker_socket(host):
    f = host.file("/var/run/docker.sock")
    assert f.exists
    assert f.is_socket

    o = host.socket("unix:///var/run/docker.sock")
    assert o.is_listening


def test_docker_storage(host):
    f = host.mount_point('/var/lib/docker')
    assert f.exists
    assert isinstance(f.options, list)
    assert 'rw' in f.options
    assert f.filesystem

    mountpoints = host.mount_point.get_mountpoints()
    assert mountpoints
    assert all(isinstance(m, host.mount_point) for m in mountpoints)
    assert len([m for m in mountpoints if m.path == "/var/lib/docker"]) == 1

