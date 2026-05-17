import sys
import logging
sys.path.insert(0, '/home/falcon/api_project')

from src.services import system

logging.basicConfig(level=logging.INFO)

def test_get_cpu():
    result = system.cpu_usage()
    assert result is not None
    assert len(result) > 0
    logging.info(f"CPU: {result[:50]}...")

def test_get_disk():
    result = system.disk_usage()
    assert result is not None
    assert "Filesystem" in result
    logging.info(f"Disk: {result[:50]}...")

def test_get_temp():
    result = system.temp()
    assert result is not None
    logging.info(f"Temp: {result[:50]}...")

def test_get_wifi():
    result = system.who_is_on_wifi()
    assert result is not None
    logging.info(f"WiFi: {result[:50]}...")

def test_get_shell():
    result = system.shell("echo Hello")
    assert "Hello" in result
    logging.info(f"Shell: {result[:50]}...")

if __name__ == "__main__":
    logging.info("Running system tests...")
    test_get_cpu()
    test_get_disk()
    test_get_temp()
    test_get_wifi()
    test_get_shell()
    logging.info("\n All system test cases passed!!")