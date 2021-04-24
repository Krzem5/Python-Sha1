def _sha1_chunk(h,dt):
	w=[]
	for i in range(0,64,4):
		w.append((dt[i]<<24)|(dt[i+1]<<16)|(dt[i+2]<<8)|dt[i+3])
	for i in range(16,80):
		v=w[i-3]^w[i-8]^w[i-14]^w[i-16]
		w.append(((v<<1)|(v>>31))&0xffffffff)
	a,b,c,d,e=h
	for i in range(80):
		if (i<20):
			f=d^(b&c)^(b&d)
			k=0x5a827999
		elif (i<40):
			f=b^c^d
			k=0x6ed9eba1
		elif (i<60):
			f=(b&c)|(b&d)|(c&d)
			k=0x8f1bbcdc
		else:
			f=b^c^d
			k=0xca62c1d6
		a,b,c,d,e=(((((a<<5)|(a>>27))&0xffffffff)+f+e+k+w[i])&0xffffffff,a,((b<<30)|(b>>2))&0xffffffff,c,d)
	return [(h[0]+a)&0xffffffff,(h[1]+b)&0xffffffff,(h[2]+c)&0xffffffff,(h[3]+d)&0xffffffff,(h[4]+e)&0xffffffff]



def sha1_start():
	return ([0x67452301,0xefcdab89,0x98badcfe,0x10325476,0xc3d2e1f0],0,b"")



def sha1_update(st,dt):
	h=st[0]
	l=st[1]+len(dt)
	dt=st[2]+dt
	while (len(dt)>=64):
		h=_sha1_chunk(h,dt[:64])
		dt=dt[64:]
	return (h,l,dt)



def sha1_end(st):
	h=st[0]
	dt=st[2]+b"\x80"+b"\x00"*((56-(st[1]+1)%64)%64)+bytes([st[1]>>53,(st[1]>>45)&0xff,(st[1]>>37)&0xff,(st[1]>>29)&0xff,(st[1]>>21)&0xff,(st[1]>>13)&0xff,(st[1]>>5)&0xff,(st[1]<<3)&0xff])
	i=0
	while (i<len(dt)):
		h=_sha1_chunk(h,dt[i:i+64])
		i+=64
	return f"{h[0]:08x}{h[1]:08x}{h[2]:08x}{h[3]:08x}{h[4]:08x}"



def sha1_simple(dt):
	h=[0x67452301,0xefcdab89,0x98badcfe,0x10325476,0xc3d2e1f0]
	l=len(dt)
	dt+=b"\x80"+b"\x00"*((56-(l+1)%64)%64)+bytes([l>>53,(l>>45)&0xff,(l>>37)&0xff,(l>>29)&0xff,(l>>21)&0xff,(l>>13)&0xff,(l>>5)&0xff,(l<<3)&0xff])
	i=0
	while (i<len(dt)):
		h=_sha1_chunk(h,dt[i:i+64])
		i+=64
	return f"{h[0]:08x}{h[1]:08x}{h[2]:08x}{h[3]:08x}{h[4]:08x}"
