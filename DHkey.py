import random
p_all=[101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251]
g_all=[2,5,2,6,3,3,2,3,2,2,6,5,2,5,2,2,2,19,5,2,3,2,3,2,6,3,7,7,6]
for i in range(len(p_all)):
        p = p_all[i]
        g = g_all[i]

        # A和B随机选择私钥
        private_key_A = random.randint(2, p - 1)
        private_key_B = random.randint(2, p - 1)

        # A计算公钥
        public_key_A = pow(g, private_key_A, p)

        # B计算公钥
        public_key_B = pow(g, private_key_B, p)

        # A和B交换公钥，计算共享密钥
        shared_key_A = pow(public_key_B, private_key_A, p)
        shared_key_B = pow(public_key_A, private_key_B, p)

        print(f"素数p: {p}")
        print(f"原根g: {g}")
        print(f"A的私钥: {private_key_A}")
        print(f"A的公钥: {public_key_A}")
        print(f"B的私钥: {private_key_B}")
        print(f"B的公钥: {public_key_B}")
        print(f"A的共享密钥: {shared_key_A}")
        print(f"B的共享密钥: {shared_key_B}")