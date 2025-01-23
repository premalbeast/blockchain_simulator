from blockchain import Blockchain

def main():
    print("Welcome to the Blockchain Simulator!")
    blockchain = Blockchain()

    while True:
        print("\n1. Add Block")
        print("2. View Blockchain")
        print("3. Validate Blockchain")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            data = input("Enter block data: ")
            blockchain.add_block(data)
            print("Block added!")
        elif choice == '2':
            for block in blockchain.chain:
                print(block)
        elif choice == '3':
            if blockchain.is_chain_valid():
                print("Blockchain is valid!")
            else:
                print("Blockchain is invalid!")
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()