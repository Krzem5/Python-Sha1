import sha1
import hashlib



h=sha1.sha1_start()
h=sha1.sha1_update(h,b"sha1_simple test ")
h=sha1.sha1_update(h,b"payload data: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
print(sha1.sha1_simple(b"sha1_simple test payload data: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"),sha1.sha1_end(h),hashlib.sha1(b"sha1_simple test payload data: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA").hexdigest())
