# Install gitlab-ee

## Installation Steps

```
andreas@spiderlounge:~$ sudo apt install gitlab-ee
Reading package lists... Done
```

### ... this takes quite some time - actually hung at:

```
GitLab was unable to detect a valid hostname for your instance.
Please configure a URL for your GitLab instance by setting `external_url`
configuration in /etc/gitlab/gitlab.rb file.
Then, you can start your GitLab instance by running the following command:
  sudo gitlab-ctl reconfigure
```

Set the URL in /etc/gitlab/gitlab.rb
Make sure you set the external_url to https 
Note: most config options are commented out in this file
Then run `sudo gitlab-ctl reconfigure`

```
sudo gitlab-ctl reconfigure
....
```

This hung as well,  need to run

```
andreas@spiderlounge:$ sudo /opt/gitlab/embedded/bin/runsvdir-start &
```

Had to copy certs to /etc/gitlab/ssl (check gitlab.rb config, it refers this directory but congifure doesn't set it up
Also had to rename /opt/gitlab/embedded/nodes/spiderlounge.us-west1-b.c.awesome-tube-294518.internal.json to /opt/gitlab/embedde/nodes/gitlab.spiderlounge.org.json and make a few edits
