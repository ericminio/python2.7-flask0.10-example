I pass level 1.1 :)

## Get ready

[fork](https://help.github.com/articles/fork-a-repo) me and [clone](https://help.github.com/articles/fork-a-repo#step-2-clone-your-fork) your repository locally.

[install python 2.7](http://www.python.org/download/)

[install fabric](http://docs.fabfile.org/en/1.8/) globally

setup your environment: in the directory of the repo, run

```sh
fab setup
```

to run all the tests

```sh
fab test
```

Test should be successful and 6 tests should pass

to run only the unit tests

```sh
fab unit
```

Test should be much faster and 3 tests should pass

[introduction to flask testing](http://flask.pocoo.org/docs/testing/)

## See it working

Lauch the application

```sh
fab run_server
```

Open your browser and navigate to

```sh
http://localhost:8080/ping
```

You should see the Json

```sh
{
  alive : true
}
```

## Deploy

Deploy and run your server so that the game can call it.
