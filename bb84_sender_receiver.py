import random

# 1. Sinh chuỗi bit ngẫu nhiên

def generate_random_bits(n):
    """
    Sinh n bit ngẫu nhiên gồm 0 và 1.

    Parameters
    ----------
    n : int
        Số lượng bit cần sinh.

    Returns
    -------
    list
        Danh sách n bit ngẫu nhiên.
    """
    return [random.randint(0, 1) for _ in range(n)]


# 2. Sinh chuỗi cơ sở ngẫu nhiên

def generate_random_bases(n):
    """
    Sinh n cơ sở đo/mã hóa ngẫu nhiên.
    Mỗi cơ sở là Z hoặc X với xác suất 1/2.

    Parameters
    ----------
    n : int
        Số lượng cơ sở cần sinh.

    Returns
    -------
    list
        Danh sách gồm 'Z' và 'X'.
    """
    return [random.choice(["Z", "X"]) for _ in range(n)]


# 3. Biểu diễn trạng thái lượng tử Alice gửi

def encode_qubit(bit, basis):
    """
    Ánh xạ bit và cơ sở thành trạng thái BB84.

    Z:
        0 -> |0>
        1 -> |1>

    X:
        0 -> |+>
        1 -> |->
    """

    if basis == "Z":
        if bit == 0:
            return "|0>"
        else:
            return "|1>"

    elif basis == "X":
        if bit == 0:
            return "|+>"
        else:
            return "|->"

    else:
        raise ValueError("Basis phải là 'Z' hoặc 'X'")


# 4. Mô phỏng phép đo lý tưởng của Bob

def ideal_measurement(alice_bit, alice_basis, bob_basis):
    """
    Mô phỏng phép đo lý tưởng trong BB84.

    Nếu Bob dùng cùng cơ sở với Alice:
        Bob thu đúng bit Alice.

    Nếu Bob dùng khác cơ sở:
        Kết quả Bob là ngẫu nhiên 0 hoặc 1.
    """

    if alice_basis == bob_basis:

        # Đúng cơ sở -> kết quả chắc chắn
        return alice_bit

    else:

        # Sai cơ sở -> kết quả ngẫu nhiên
        return random.randint(0, 1)


# 5. Bob đo toàn bộ chuỗi qubit

def measure_sequence(alice_bits, alice_bases, bob_bases):
    """
    Bob tiến hành đo toàn bộ các qubit Alice gửi.
    """

    bob_results = []

    for alice_bit, alice_basis, bob_basis in zip(
        alice_bits,
        alice_bases,
        bob_bases
    ):

        result = ideal_measurement(
            alice_bit,
            alice_basis,
            bob_basis
        )

        bob_results.append(result)

    return bob_results


# 6. Chương trình demo BB84

def run_demo(n=16):

    # Alice

    alice_bits = generate_random_bits(n)

    alice_bases = generate_random_bases(n)

    alice_states = [
        encode_qubit(bit, basis)
        for bit, basis in zip(alice_bits, alice_bases)
    ]


    # Bob

    bob_bases = generate_random_bases(n)

    bob_results = measure_sequence(
        alice_bits,
        alice_bases,
        bob_bases
    )


    # Hiển thị kết quả

    print("=" * 75)
    print("MÔ PHỎNG TRUYỀN VÀ ĐO QUBIT BB84")
    print("=" * 75)

    print(
        f"{'i':<4}"
        f"{'A-bit':<8}"
        f"{'A-basis':<10}"
        f"{'State':<10}"
        f"{'B-basis':<10}"
        f"{'B-result':<10}"
        f"{'Match':<8}"
    )

    print("-" * 75)

    for i in range(n):

        match = (
            "YES"
            if alice_bases[i] == bob_bases[i]
            else "NO"
        )

        print(
            f"{i:<4}"
            f"{alice_bits[i]:<8}"
            f"{alice_bases[i]:<10}"
            f"{alice_states[i]:<10}"
            f"{bob_bases[i]:<10}"
            f"{bob_results[i]:<10}"
            f"{match:<8}"
        )


    print("\nAlice bits : ", alice_bits)
    print("Alice bases: ", alice_bases)
    print("Bob bases  : ", bob_bases)
    print("Bob results: ", bob_results)



# Main

if __name__ == "__main__":

    run_demo(16)
