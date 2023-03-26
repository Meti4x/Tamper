# Report Vulnerability

Always look at Program’s report policy before writing one, some program’s have their own templates. And if not here’s a general one to fallow through

```markdown
## Summary
A brief summery of what is the vulnerability about and mention the vulnerable domain.

## Description
Describe the vulnerability as much  details you could to cover.

## PoC or steps to Reproduce
Sreps to reproduce the vulnerability and pictures in the end.

## Impact 
Mention your reasons as to how the vulnerability could affect the system and company.

(Optionals)
## Mitigation
Your suggestion to (Possible) fix the bug.

# Reference
Link to reference other platform's reports or articles for more information.
```

- A vulnerability and report without PoC is nothing, so stop reporting it.
- Always look at program’s policy as to how behave when finding a bug. (e.g. Don’t upload malicious file if other extensions allowed).
- Always look at out-of-scope domains in policy (Tip: better to avoid working on them most of the time)
- Always look at out-of-scope vulnerability before working on a particular bug type or reporting an issue.
- Sometimes record a brief video demonstrating the bug especially P1 ones, in case if platform’s team can’t reproduce the bug for whatever reason.
- When recording a video, be sure that URL is within video’s frame.
- Highlight key point’s in pictures that you want to emphasize on e.g. parameter that is vulnerable to IDOR
- Avoid write many words in the report. if you can, describe in fewer words.
- Generally, It’s better to test all bug type’s on your own accounts not other User’s.

## English tips

- check your report in an online website to check the grammar.
- Avoid believe passive aggressive (i.e Why my report is not triaged? - this impact is high and you’re wrong)
    - If you disagree with Report’s state or decision made,  use words like believe, think, would like to mention etc. e.g. I believe that vulnerability could have high impact based on reasons I mentioned.

## General tips on reporting different bug classes

- XSS
    - **Always** use window.origin or document.location for alert() PoC. ( Don’t put your own name :) )
    - **Always** include the URL in taking pictures when XSS being triggered.
    - Include the XSS payload in report.
- IDOR
    - **Always** test IDORs on your own accounts.
    - Take pictures of tow compromised accounts and mention the tow accounts’ ID and other information etc.
- RCE
    - Create a tmp.txt file in /tmp directory which contains some words you mention in report
    - Better to avoid searching for sensitive file (/etc/passwd) as most of the program’s nowadays have a policy against doing that. instead to what is mentioned above.
- SSRF
    - It’s fine to go for internal port scanning or AWS and other cloud metadata’s (Although checking the policy before doing that would be good)
- Information Disclosure (PII)
    - Avoid dumping all data, showing one sample would be enough.
- SQL Injection
    - Avoid dumping database (Ask before doing that)
    - For PoC showing something like server’s delay response to sleep(5) request would be sufficient.
- Subdomain Takeover’s
    - Don’t report it before hosting a PoC file on vulnerable target.
- API leakage
    - Always look for a PoC, if you want to report without PoC, expect the report to be marked as NA :-)
- CORS Misconfiguration
    - Don’t need to buy a domain (Find a bypass like [attackyahoo.co](http://attackyahoo.co)m) to show PoC. instead edit your /etc/hosts file mapping the domain to

## Example of report vulnerability

```markdown
## Summery 

```
