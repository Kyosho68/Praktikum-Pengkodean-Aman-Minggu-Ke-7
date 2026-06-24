from threading import Thread, Lock
from time import sleep


class Voucher:

    def __init__(self):
        self.used = False
        self.used_by = None
        self.lock = Lock()

    def use(self, user):

        with self.lock:

            if self.used:
                print(user, "GAGAL, voucher sudah dipakai")
                return

            sleep(0.1)

            self.used = True
            self.used_by = user

            print(user, "BERHASIL memakai voucher")


print("=== SUCCESS + FAILURE CASE ===")

voucher = Voucher()

t1 = Thread(target=voucher.use, args=("alice",))
t2 = Thread(target=voucher.use, args=("bob",))

t1.start()
t2.start()

t1.join()
t2.join()

print("\nFinal voucher state:")
print(voucher.__dict__)
