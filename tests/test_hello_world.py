import pytest
from hello_world.hello_world import print_message

class TestPrintMessage(object):
  def test_larger_than_zero(self):
    with pytest.raises(ValueError) as exc_info:
      print_message(-2,"Hello")
    expected_error_msg = "Argument must be >=1"
    assert exc_info.match(expected_error_msg)
