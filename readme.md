## Everything in this repo is from the year 2019-2020. Dates of commits don't indicate that, as I needed to delete sensitive data.

### Instead of using `git filter-repo --invert-paths --path winService --force` to delete sensitive data, I experimented with `git rebase` which messed up dates of commits.

The software in this repo was a test of antivirus detection, and both signature-based detection and heuristic analysis failed miserably for the antivirus software, including after "compiling" to .exe file.

The test also included services such as www.virustotal.com.

Back then (2019-2020), and perhaps still today, antivirus software simply couldn't cope with potentially malicious or self-hiding software written in interpreter-type languages. This is a lesson in security, and potentially in not running freeware closed-source software. Probabilites in this case add up with each closed-source software used. Virtual-machines/Sandboxie or similar should be more of a standard.
