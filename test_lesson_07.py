import subprocess

def test_lesson_07():
    result = subprocess.run(['python3', 'lesson_07.py'], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    assert "apple" in output[0] and "cherry" in output[0], f"Failed TODO 1: {output[0]}"
    assert "orange" in output[1] and "banana" not in output[1], f"Failed TODO 2: {output[1]}"
    assert "apple" in output[2] and "banana" in output[2], f"Failed TODO 3: {output[2]}"
    assert "cherry" in output[3], f"Failed TODO 4: {output[3]}"
    assert "4" in output[4] and "16" in output[4], f"Failed TODO 5: {output[4]}"
    assert "6" in output[5], f"Failed TODO 6: {output[5]}"
    assert "[1 2 3 4 5]" in output[6], f"Failed TODO 7: {output[6]}"
    assert "3" in output[7] and "10" in output[7], f"Failed TODO 8: {output[7]}"
    assert "True" in output[8], f"Failed TODO 9: {output[8]}"
    assert "fixed" in output[9], f"Failed TODO 10: {output[9]}"

    print("Lesson 7: All tests passed!")

if __name__ == "__main__":
    test_lesson_07()
