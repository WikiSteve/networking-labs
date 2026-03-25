# Test and Log Multiple Targets

The last step is to reuse your script against several targets and save the results to a file.

This is where Part 1 comes back:

- `done < targets.txt` redirects standard input from a file
- `2>&1` combines `stderr` with `stdout`
- `tee` shows the output on screen and writes it to a file

## Create a target list

Create a small file named `targets.txt`.

```bash
nano targets.txt
```

Enter these lines:

```text
localhost
192.0.2.1
definitely-not-a-real-hostname.invalid
```

Save the file.

## Run a batch test and save the output

Remove any old results file so you can see a clean run.

```bash
rm -f batch-results.txt
```

Run this loop exactly as written:

```bash
while read -r TARGET; do
  echo "Testing $TARGET"
  ./hostcheck.sh "$TARGET"
  echo "Exit code: $?"
  echo
done < targets.txt 2>&1 | tee batch-results.txt
```

This should produce:

- at least one `UP:` result
- at least one `No reply` result
- at least one `DNS lookup failed` result

It should also save the same output to `batch-results.txt`.

## View the saved file

```bash
cat batch-results.txt
```

## Optional: append instead of replace

If you want to keep previous test runs instead of replacing them, rerun the loop with:

```bash
done < targets.txt 2>&1 | tee -a batch-results.txt
```

That `-a` switch appends instead of clobbering the file.

## **Screenshot 6: Batch Test Logged with tee**
**Requirement:** In one screenshot, show all four of these:

- `cat targets.txt`
- the `while read -r TARGET` loop command
- visible output that includes one `UP:` result, one `No reply` result, and one `DNS lookup failed` result
- `cat batch-results.txt` proving the results were saved to a file

---
[Prev](04_test-success-and-failure.md) | [Home](README.md) | [Next](06_submission-guide.md)
