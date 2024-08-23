Issue Summary:
Outage Duration:

Start Time: 2024-08-22 14:00 UTC
End Time: 2024-08-22 15:30 UTC
Total Duration: 1 hour 30 minutes of pure adrenaline
Impact:

It was a tough hour and a half for 80% of our users, who found themselves locked out of the platform, frantically refreshing the page in hopes of logging in. The login service was taking a well-deserved (but unscheduled) break, leaving users hanging.
Root Cause:

A tiny, sneaky misconfiguration in our Nginx server decided to play hide and seek, leading to our server not handling requests properly. Who knew one line could cause so much drama?
Timeline:
14:00 UTC: The trouble begins. Our trusty monitoring alert goes off, screaming about a surge in failed login attempts. The alarm bells were ringing, and panic mode was initiated.

14:05 UTC: The engineering squad dives in, armed with coffee and determination. The first suspect? The database—because, let's face it, it’s usually the database.

14:15 UTC: Plot twist! The database is innocent. The team shifts its focus to the application server, hoping for a quick fix.

14:25 UTC: A wild goose chase through the application code reveals... absolutely nothing. The frustration levels rise as time ticks away.

14:40 UTC: The big guns are called in. The incident is escalated to the DevOps team, who enter the scene with a dramatic flair.

15:00 UTC: The culprit is found hiding in the Nginx configuration file. It turns out, a missing line was causing all the chaos. Classic.

15:10 UTC: The rogue line is restored to its rightful place. The server is rebooted, and the login service slowly comes back to life.

15:30 UTC: The dust settles. The service is fully restored, and users can finally log in again. Crisis averted—time for a collective sigh of relief.

Root Cause and Resolution:
Detailed Explanation:

Our Nginx configuration got a bit of an unintentional haircut during a recent update, leaving out a critical line responsible for directing traffic. This meant that when users tried to log in, the requests were basically lost in the void. Oops.
Fix:

We swiftly added the missing line back into the Nginx configuration, double-checked everything like paranoid detectives, and restarted the server. With that, order was restored, and the login service was back in action.
Corrective and Preventative Measures:
Improvements:

We learned our lesson the hard way—testing, testing, and more testing before making changes. And let’s not forget about better monitoring to catch these sneaky misconfigurations before they wreak havoc.
Tasks:

[ ] Patch the Nginx configuration and give it a thorough review.
[ ] Set up a specific monitoring alert to catch any future Nginx shenanigans.
[ ] Implement a rollback procedure for configuration changes—because backups are our best friend.
