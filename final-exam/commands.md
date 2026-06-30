# commands.md — exact commands I ran, per part

> Paste the **real** commands you ran, in order, in the fenced blocks below. Graded for
> command competency and is your defence if any output is questioned. One block per part.
> Delete the hint comments and replace with your actual commands.

## Part A — Threads, Mapping & Signals

```bash
# compile the threaded program (mind the threading flag), run it
# capture the 1:1 user→kernel (LWP) mapping into thread_map.txt while it runs
# compile/run signal_demo and demonstrate catching the interactive interrupt
cd ~/os-se-p20240003/final-exam/partA_threads
gcc -pthread thread_demo.c -o thread_demo
./thread_demo

gcc signal_demo.c -o signal_demo
./signal_demo
# (pressed Ctrl+C to send SIGINT)
```

## Part B — Permissions, Special Bits & ACLs

```bash
# build the tree (shared dir + private file); set octal + symbolic modes
# demonstrate setgid + sticky on a dir you own; build/set the setuid binary
# add and read back an ACL entry; save reports
mkdir -p partB_security/permtree/shared
cd partB_security/permtree
touch private.txt
chmod 600 private.txt
chmod u=rwx,g=rx,o=x shared
ls -l private.txt; ls -ld shared; stat private.txt; stat shared > perm_report.txt

mkdir setgid_dir
chmod g+s setgid_dir
touch setgid_dir/testfile
ls -ld setgid_dir
ls -l setgid_dir/testfile

mkdir sticky_dir
chmod 1777 sticky_dir
ls -ld sticky_dir

gcc setuid_demo.c -o setuid_demo
chmod u+s setuid_demo
ls -l setuid_demo
./setuid_demo
```

## Part C — Bash Scripting, PATH & Safe Scanning

```bash
# make greeter runnable by name via PATH; record PATH + resolved location
# run collector over your dirs; show it skips unreadable/missing files safely
mkdir -p ~/bin
nano ~/bin/greeter
chmod +x ~/bin/greeter
greeter
which greeter
echo $PATH

mkdir -p partC_scripting/data1 partC_scripting/data2
echo "file1 contents" > partC_scripting/data1/a.txt
echo "file2 contents" > partC_scripting/data2/b.txt
echo "secret stuff" > partC_scripting/data1/locked.txt
chmod 000 partC_scripting/data1/locked.txt

nano ~/bin/collector
chmod +x ~/bin/collector
collector
cat partC_scripting/collector_report.txt

cp ~/bin/greeter partC_scripting/scripts/greeter
cp ~/bin/collector partC_scripting/scripts/collector
```

## Part D — Race Condition & flock

```bash
# init stock; run swarm several times unpatched and record final stock each time
# add the exclusive advisory lock around the read-modify-write; re-run swarm
mkdir -p partD_secure/data
echo 100 > partD_secure/data/stock.txt

nano ~/bin/buy_beacon
chmod +x ~/bin/buy_beacon
buy_beacon alice 5
cat partD_secure/data/stock.txt
cat partD_secure/data/sales.log
cp ~/bin/buy_beacon partD_secure/scripts/buy_beacon

nano ~/bin/buy_beacon_unsafe
chmod +x ~/bin/buy_beacon_unsafe

nano ~/bin/swarm
chmod +x ~/bin/swarm
cp ~/bin/swarm partD_secure/scripts/swarm

# D2 - unpatched race demo
for i in 1 2 3; do
  echo "=== Run $i ==="
  echo 100 > partD_secure/data/stock.txt
  swarm buy_beacon_unsafe
done | tee partD_secure/observations.txt

# D3 - patched version, deterministic
echo 100 > partD_secure/data/stock.txt
swarm buy_beacon
cat partD_secure/data/stock.txt
```

## Part E — Backups & cron

```bash
# E1: run backup_project enough times that pruning happens (keep newest RETAIN_N)
# E2: per-user crontab, two entries (absolute paths):
#     recurring (CRON_INTERVAL) -> partE_automation/logs/cron_recurring.log
#     one-shot at TIMED        -> partE_automation/logs/cron_oneshot.log
# E3: backup_exam -> tar the final-exam folder to ~/exam-backups/final-exam-<ts>.tar.gz
#     crontab: run backup_exam on a short interval AND once at exactly 16:00 today
#     then: ls ~/exam-backups
# capture crontab -l + both logs + the ~/exam-backups listing into cron_report.txt
<your commands>
```
