from threading import Thread
from time import sleep


class Voucher:

    def __init__(self):
        self.used = False
        self.used_by = None


class VoucherService:

    def use(self, voucher, user):

        # TIME OF CHECK
        if voucher.used:
            print(user, "voucher sudah dipakai")
            return

        sleep(0.1)

        # TIME OF USE
        voucher.used = True
        voucher.used_by = user

        print(user, "BERHASIL memakai voucher")


print("=== FAILURE CASE ===")

voucher = Voucher()

service = VoucherService()

t1 = Thread(target=service.use, args=(voucher, "alice"))
t2 = Thread(target=service.use, args=(voucher, "bob"))

t1.start()
t2.start()

t1.join()
t2.join()

print("\nFinal voucher state:")
print(voucher.__dict__)

print("\nMasalah:")
print("Voucher dipakai dua kali.")
