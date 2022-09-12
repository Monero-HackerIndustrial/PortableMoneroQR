# Portable Monero QR

The portable monero qr standard is the standard created for the monerosigner project.

## Why?
The portable QR standard is a compression/pagination standard for data frames for offline data transfer. There has been a lot of different projects through the years but they didn't deal with the smaller device constraints. (Samller devices contain smaller screens and cheap/lowres cameras)


## How does it work?

The Portable QR code standard breaks larger files into smaller frames of encoded data. Each frame is a QR code. The QR code can be animated at a variable fps offset which starts fast but gets slower over time. The fps offset is optimized for slow row res cameras but doesn't hinder faster quality cameras as it starts with a faster fps and eventually slows down to slower for slower cameras.

A simple transfer like that is basically a base64 json with the following data in each frame:
```
frame = {
"index" = 0,
"total" = 8,
"data" = base64(data)
}
```

The frame data is included with each frame which means order received for the data doesn't matter as the end application can reconstruct the data and decode it.

## Possible improvements

 I like the idea of including a hash scheme to prevent broken data frames but QR codes already have built in error correction.
 PGP Support (for offline signing)

## Research needed

I need to research how accurate the QR codes are with how much data I pack in them. The more data you pack into a qr code the less fidelity there is for error correcting. I will test different data payloads to view which one works the best with the monerosigner camera.

I will reseach the best fps for the monerosigner camera. There should be a good offset which helps the device pull data faster as scans from the camera take time to process.

I will research the optimal rate increase in FPS for best coverage of both fast and slow cameras. 
