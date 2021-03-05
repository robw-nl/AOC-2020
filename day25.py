def main():
    val = key = 1
    for loop_size in range(1, 20201227):
        val = (7 * val) % 20201227
        if val == 10212254:
            break

    for _ in range(loop_size):
        key = (key * 12577395) % 20201227
    print(key)

if __name__ == '__main__':   
        main()