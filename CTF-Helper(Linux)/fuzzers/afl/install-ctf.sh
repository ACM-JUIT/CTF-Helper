wget http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz
tar xzf afl-latest.tgz 
rm afl-latest.tgz
mv afl-*/ afl
cd afl
ls -la 
make

cd qemu_mode
sudo apt-get install -y bison libglib2.0-dev
./build_qemu_support.sh
cd ../..

