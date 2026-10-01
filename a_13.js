// Lab 1A, A.13: decompress the Base64 strings (zlib/deflate format)
const zlib = require('zlib');
for (const s of ['eJzzyc9Lyc8DAAgpAms=', 'eJxzSi3KycwDAAfXAl0=', 'eJzzSy1XiMwvygYADKUC8A==']) {
  console.log(zlib.inflateSync(Buffer.from(s, 'base64')).toString());
}
