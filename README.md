# vercel-bug-python-function-file-open

Issue: Attempting to read file manually fails. Flasks inbuilt send_file still works

Description:

1. Inspect `https://vercel-bug-python-function-file-open.vercel.app/api/working` that returns `Hello World` from `file.txt`.
2. Inspect `https://vercel-bug-python-function-file-open.vercel.app/api/not-working` that failed to return. Inspect Function logs to see stacktrace.