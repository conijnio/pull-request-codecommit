# CHANGELOG



## v0.5.9 (2024-03-04)

### Chore

* chore: disable long_description ([`5df187b`](https://github.com/conijnio/pull-request-codecommit/commit/5df187b14918fce44717d39ae1f6756c6c6aef32))


## v0.5.8 (2024-03-04)

### Chore

* chore: enable token again ([`15573c5`](https://github.com/conijnio/pull-request-codecommit/commit/15573c5d0d6f4f8b74806508bcfc928cc95d3fa6))


## v0.5.7 (2024-03-04)

### Chore

* chore: add built command ([`67a4ca4`](https://github.com/conijnio/pull-request-codecommit/commit/67a4ca47fe81d03ffbf2ca32d5f605533aa3f07c))


## v0.5.6 (2024-03-04)

### Chore

* chore: implement pypi publishing ([`de39102`](https://github.com/conijnio/pull-request-codecommit/commit/de391027ae9f739a4c217d2ecd6e6854bd968db8))


## v0.5.5 (2024-03-04)

### Chore

* chore: tweak release ([`5f3f5a4`](https://github.com/conijnio/pull-request-codecommit/commit/5f3f5a40a1107ee2ef00908dac65c23fb93cfdc9))

* chore: remove built command ([`d6fd3ec`](https://github.com/conijnio/pull-request-codecommit/commit/d6fd3ece0bfdcb8f3e3c1f594b5ebd2daff7e093))


## v0.5.4 (2024-03-04)

### Chore

* chore: tweak semantic release config ([`5e916b9`](https://github.com/conijnio/pull-request-codecommit/commit/5e916b95f9522c115941684dac08949365864b02))

* chore: move repository to organization

I want to manage the open source repos that I maintain from an organization. ([`81f22ba`](https://github.com/conijnio/pull-request-codecommit/commit/81f22ba47a72c2682f6baa70923a38659a5b69e7))

* chore(deps-dev): bump pytest from 8.0.2 to 8.1.0 (#189)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.0.2 to
8.1.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;8.1.0&lt;/h2&gt;
&lt;h1&gt;pytest 8.1.0 (2024-03-03)&lt;/h1&gt;
&lt;h2&gt;Features&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11475&#34;&gt;#11475&lt;/a&gt;:
Added the new &lt;code&gt;consider_namespace_packages&lt;/code&gt;{.interpreted-text
role=&amp;quot;confval&amp;quot;} configuration option, defaulting to
&lt;code&gt;False&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If set to &lt;code&gt;True&lt;/code&gt;, pytest will attempt to identify modules
that are part of &lt;a
href=&#34;https://packaging.python.org/en/latest/guides/packaging-namespace-packages&#34;&gt;namespace
packages&lt;/a&gt; when importing modules.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11653&#34;&gt;#11653&lt;/a&gt;:
Added the new &lt;code&gt;verbosity_test_cases&lt;/code&gt;{.interpreted-text
role=&amp;quot;confval&amp;quot;} configuration option for fine-grained control
of test execution verbosity.
See &lt;code&gt;Fine-grained verbosity
&amp;lt;pytest.fine_grained_verbosity&amp;gt;&lt;/code&gt;{.interpreted-text
role=&amp;quot;ref&amp;quot;} for more details.&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Improvements&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/10865&#34;&gt;#10865&lt;/a&gt;:
&lt;code&gt;pytest.warns&lt;/code&gt;{.interpreted-text role=&amp;quot;func&amp;quot;} now
validates that &lt;code&gt;warnings.warn&lt;/code&gt;{.interpreted-text
role=&amp;quot;func&amp;quot;} was called with a [str]{.title-ref} or a
[Warning]{.title-ref}.
Currently in Python it is possible to use other types, however this
causes an exception when
&lt;code&gt;warnings.filterwarnings&lt;/code&gt;{.interpreted-text
role=&amp;quot;func&amp;quot;} is used to filter those warnings (see [CPython &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/103577&#34;&gt;#103577&lt;/a&gt;](&lt;a
href=&#34;https://redirect.github.com/python/cpython/issues/103577&#34;&gt;python/cpython#103577&lt;/a&gt;)
for a discussion).
While this can be considered a bug in CPython, we decided to put guards
in pytest as the error message produced without this check in place is
confusing.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11311&#34;&gt;#11311&lt;/a&gt;:
When using &lt;code&gt;--override-ini&lt;/code&gt; for paths in invocations without
a configuration file defined, the current working directory is used
as the relative directory.&lt;/p&gt;
&lt;p&gt;Previoulsy this would raise an
&lt;code&gt;AssertionError&lt;/code&gt;{.interpreted-text
role=&amp;quot;class&amp;quot;}.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11475&#34;&gt;#11475&lt;/a&gt;:
&lt;code&gt;--import-mode=importlib
&amp;lt;import-mode-importlib&amp;gt;&lt;/code&gt;{.interpreted-text
role=&amp;quot;ref&amp;quot;} now tries to import modules using the standard
import mechanism (but still without changing
:py&lt;code&gt;sys.path&lt;/code&gt;{.interpreted-text role=&amp;quot;data&amp;quot;}),
falling back to importing modules directly only if that fails.&lt;/p&gt;
&lt;p&gt;This means that installed packages will be imported under their
canonical name if possible first, for example
&lt;code&gt;app.core.models&lt;/code&gt;, instead of having the module name always
be derived from their path (for example
&lt;code&gt;.env310.lib.site_packages.app.core.models&lt;/code&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11801&#34;&gt;#11801&lt;/a&gt;:
Added the &lt;code&gt;iter_parents()
&amp;lt;_pytest.nodes.Node.iter_parents&amp;gt;&lt;/code&gt;{.interpreted-text
role=&amp;quot;func&amp;quot;} helper method on nodes.
It is similar to &lt;code&gt;listchain
&amp;lt;_pytest.nodes.Node.listchain&amp;gt;&lt;/code&gt;{.interpreted-text
role=&amp;quot;func&amp;quot;}, but goes from bottom to top, and returns an
iterator, not a list.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11850&#34;&gt;#11850&lt;/a&gt;:
Added support for &lt;code&gt;sys.last_exc&lt;/code&gt;{.interpreted-text
role=&amp;quot;data&amp;quot;} for post-mortem debugging on Python&amp;gt;=3.12.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11962&#34;&gt;#11962&lt;/a&gt;:
In case no other suitable candidates for configuration file are found, a
&lt;code&gt;pyproject.toml&lt;/code&gt; (even without a
&lt;code&gt;[tool.pytest.ini_options]&lt;/code&gt; table) will be considered as the
configuration file and define the &lt;code&gt;rootdir&lt;/code&gt;.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11978&#34;&gt;#11978&lt;/a&gt;:
Add &lt;code&gt;--log-file-mode&lt;/code&gt; option to the logging plugin, enabling
appending to log-files. This option accepts either
&lt;code&gt;&amp;quot;w&amp;quot;&lt;/code&gt; or &lt;code&gt;&amp;quot;a&amp;quot;&lt;/code&gt; and defaults to
&lt;code&gt;&amp;quot;w&amp;quot;&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Previously, the mode was hard-coded to be &lt;code&gt;&amp;quot;w&amp;quot;&lt;/code&gt;
which truncates the file before logging.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12047&#34;&gt;#12047&lt;/a&gt;:
When multiple finalizers of a fixture raise an exception, now all
exceptions are reported as an exception group.
Previously, only the first exception was reported.&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11904&#34;&gt;#11904&lt;/a&gt;:
Fixed a regression in pytest 8.0.0 that would cause test collection to
fail due to permission errors when using &lt;code&gt;--pyargs&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;This change improves the collection tree for tests specified using
&lt;code&gt;--pyargs&lt;/code&gt;, see &lt;code&gt;12043&lt;/code&gt;{.interpreted-text
role=&amp;quot;pull&amp;quot;} for a comparison with pytest 8.0 and &amp;lt;8.&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/b9a167f9bbbd6eda4f0360c5bf5b7f5af50f2bc4&#34;&gt;&lt;code&gt;b9a167f&lt;/code&gt;&lt;/a&gt;
Prepare release version 8.1.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/00043f7f1047b29fdaeb18e169fe9d6146988cb8&#34;&gt;&lt;code&gt;00043f7&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12038&#34;&gt;#12038&lt;/a&gt;
from bluetech/fixtures-rm-arg2index&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/f4e10251a4a003495b5228cea421d4de5fa0ce89&#34;&gt;&lt;code&gt;f4e1025&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12048&#34;&gt;#12048&lt;/a&gt;
from bluetech/fixture-teardown-excgroup&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/43492f5707b38dab9b62dfb829bb41a13579629f&#34;&gt;&lt;code&gt;43492f5&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12051&#34;&gt;#12051&lt;/a&gt;
from jakkdl/test_debugging_pythonbreakpoint&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/82fe28dae4eec900123175cee87245f37b964e5c&#34;&gt;&lt;code&gt;82fe28d&lt;/code&gt;&lt;/a&gt;
[automated] Update plugin list (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12049&#34;&gt;#12049&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/5e2ee7175c145f84ff9882be9496abb56e6e56f2&#34;&gt;&lt;code&gt;5e2ee71&lt;/code&gt;&lt;/a&gt;
monkeypatch.delenv PYTHONBREAKPOINT in two tests that previously
failed/skipped&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/89ee4493ccbcd118349082cd78eb52a761683120&#34;&gt;&lt;code&gt;89ee449&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11997&#34;&gt;#11997&lt;/a&gt;
from nicoddemus/11475-importlib&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/8248946a552635f5751a58c7a6dfd24e98db7404&#34;&gt;&lt;code&gt;8248946&lt;/code&gt;&lt;/a&gt;
Do not collect symlinked tests under Windows (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12050&#34;&gt;#12050&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/434282e17f5f1f4fcc1464a0a0921cf19804bdd7&#34;&gt;&lt;code&gt;434282e&lt;/code&gt;&lt;/a&gt;
fixtures: use exception group when multiple finalizers raise in fixture
teardown&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d6134bc21e27efee7a2e264bd089e6c223515904&#34;&gt;&lt;code&gt;d6134bc&lt;/code&gt;&lt;/a&gt;
doc: document consider_namespace_packages option&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/8.0.2...8.1.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=8.0.2&amp;new-version=8.1.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`72d03b9`](https://github.com/conijnio/pull-request-codecommit/commit/72d03b9ae610218a836456f15205a469d5cdb2e5))

* chore(deps-dev): bump pytest from 8.0.1 to 8.0.2 (#188)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.0.1 to
8.0.2.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;8.0.2&lt;/h2&gt;
&lt;h1&gt;pytest 8.0.2 (2024-02-24)&lt;/h1&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11895&#34;&gt;#11895&lt;/a&gt;:
Fix collection on Windows where initial paths contain the short version
of a path (for example &lt;code&gt;c:\PROGRA~1\tests&lt;/code&gt;).&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11953&#34;&gt;#11953&lt;/a&gt;:
Fix an &lt;code&gt;IndexError&lt;/code&gt; crash raising from
&lt;code&gt;getstatementrange_ast&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12021&#34;&gt;#12021&lt;/a&gt;:
Reverted a fix to [--maxfail]{.title-ref} handling in pytest 8.0.0
because it caused a regression in pytest-xdist whereby session fixture
teardowns may get executed multiple times when the max-fails is
reached.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/31afeeb0df0e8bdab1325b5992a2cc733e981e82&#34;&gt;&lt;code&gt;31afeeb&lt;/code&gt;&lt;/a&gt;
Prepare release version 8.0.2&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/1b00a2f4fba7859c31dab4f5afdd9e1f07cbdd1e&#34;&gt;&lt;code&gt;1b00a2f&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12025&#34;&gt;#12025&lt;/a&gt;
from pytest-dev/backport-12022-to-8.0.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/ff2f66d84affb0fbcbf841b1897c7599026730bc&#34;&gt;&lt;code&gt;ff2f66d&lt;/code&gt;&lt;/a&gt;
[8.0.x] Revert &amp;quot;Fix teardown error reporting when
&lt;code&gt;--maxfail=1&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11721&#34;&gt;#11721&lt;/a&gt;)&amp;quot;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/8a8eed609c3c20da452446e1686df41ebda96d11&#34;&gt;&lt;code&gt;8a8eed6&lt;/code&gt;&lt;/a&gt;
[8.0.x] Fix collection of short paths on Windows (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12024&#34;&gt;#12024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/74346f027c205e5daffe66801094293744e8d85f&#34;&gt;&lt;code&gt;74346f0&lt;/code&gt;&lt;/a&gt;
[8.0.x] Allow Sphinx 7.x (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12005&#34;&gt;#12005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/b7657b4d6b69ee26e00d9a71c4d208506f644462&#34;&gt;&lt;code&gt;b7657b4&lt;/code&gt;&lt;/a&gt;
[8.0.x] Disallow Sphinx 6 and 7 (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12001&#34;&gt;#12001&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/feb7c5e12ee3374b2c7c773614d76811ad21a4f4&#34;&gt;&lt;code&gt;feb7c5e&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11999&#34;&gt;#11999&lt;/a&gt;
from pytest-dev/backport-11996-to-8.0.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/090965574ece50c6be955719ced2a9cf8daaee17&#34;&gt;&lt;code&gt;0909655&lt;/code&gt;&lt;/a&gt;
[8.0.x] code: fix &lt;code&gt;IndexError&lt;/code&gt; crash in
&lt;code&gt;getstatementrange_ast&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/68524d48586e7f8d070fc1146e5ff90e770d0382&#34;&gt;&lt;code&gt;68524d4&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11993&#34;&gt;#11993&lt;/a&gt;
from pytest-dev/release-8.0.1&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/8.0.1...8.0.2&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=8.0.1&amp;new-version=8.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`f6cc25b`](https://github.com/conijnio/pull-request-codecommit/commit/f6cc25b6ab8b9c606e3a8ddf77ea7eee9c768ddc))

* chore(deps-dev): bump cryptography from 42.0.2 to 42.0.4 (#187)

Bumps [cryptography](https://github.com/pyca/cryptography) from 42.0.2
to 42.0.4.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst&#34;&gt;cryptography&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;42.0.4 - 2024-02-20&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;
* Fixed a null-pointer-dereference and segfault that could occur when
creating
a PKCS#12 bundle. Credit to **Alexander-Programming** for reporting the
  issue. **CVE-2024-26130**
* Fixed ASN.1 encoding for PKCS7/SMIME signed messages. The fields
``SMIMECapabilities``
and ``SignatureAlgorithmIdentifier`` should now be correctly encoded
according to the
  definitions in :rfc:`2633` :rfc:`3370`.
&lt;p&gt;.. _v42-0-3:&lt;/p&gt;
&lt;p&gt;42.0.3 - 2024-02-15
&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Fixed an initialization issue that caused key loading failures for
some
users.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;.. _v42-0-2:&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/fe18470f7d05f963e7267e34fdf985d81ea6ceea&#34;&gt;&lt;code&gt;fe18470&lt;/code&gt;&lt;/a&gt;
Bump for 42.0.4 release (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10445&#34;&gt;#10445&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/aaa2dd06ed470695de818405a982d4c459869803&#34;&gt;&lt;code&gt;aaa2dd0&lt;/code&gt;&lt;/a&gt;
Fix ASN.1 issues in PKCS#7 and S/MIME signing (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10373&#34;&gt;#10373&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10442&#34;&gt;#10442&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/7a4d012991061974da5d9cb7614de65eac94f49b&#34;&gt;&lt;code&gt;7a4d012&lt;/code&gt;&lt;/a&gt;
Fixes &lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10422&#34;&gt;#10422&lt;/a&gt;
-- don&#39;t crash when a PKCS#12 key and cert don&#39;t match (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10423&#34;&gt;#10423&lt;/a&gt;)
...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/df314bb182bdfd661333969a94325e4680d785f6&#34;&gt;&lt;code&gt;df314bb&lt;/code&gt;&lt;/a&gt;
backport actions m1 switch to 42.0.x (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10415&#34;&gt;#10415&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/c49a7a5271178c6e8ef36fa1c499f62c63ec19b9&#34;&gt;&lt;code&gt;c49a7a5&lt;/code&gt;&lt;/a&gt;
changelog and version bump for 42.0.3 (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10396&#34;&gt;#10396&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/396bcf64c5be826ec00e7d7f45838c858c049cbc&#34;&gt;&lt;code&gt;396bcf6&lt;/code&gt;&lt;/a&gt;
fix provider loading take two (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10390&#34;&gt;#10390&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10395&#34;&gt;#10395&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/0e0e46f5f73f477b8ee9682738c42129d5d60177&#34;&gt;&lt;code&gt;0e0e46f&lt;/code&gt;&lt;/a&gt;
backport: initialize openssl&#39;s legacy provider in rust (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10323&#34;&gt;#10323&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10333&#34;&gt;#10333&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/pyca/cryptography/compare/42.0.2...42.0.4&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cryptography&amp;package-manager=pip&amp;previous-version=42.0.2&amp;new-version=42.0.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/pull-request-codecommit/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`45ebaa7`](https://github.com/conijnio/pull-request-codecommit/commit/45ebaa73b5382289112fa8b172b020c9d6185253))

* chore(deps-dev): bump pytest from 8.0.0 to 8.0.1 (#186)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.0.0 to
8.0.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;8.0.1&lt;/h2&gt;
&lt;h1&gt;pytest 8.0.1 (2024-02-16)&lt;/h1&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11875&#34;&gt;#11875&lt;/a&gt;:
Correctly handle errors from
&lt;code&gt;getpass.getuser&lt;/code&gt;{.interpreted-text role=&amp;quot;func&amp;quot;} in
Python 3.13.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11879&#34;&gt;#11879&lt;/a&gt;:
Fix an edge case where &lt;code&gt;ExceptionInfo._stringify_exception&lt;/code&gt;
could crash &lt;code&gt;pytest.raises&lt;/code&gt;{.interpreted-text
role=&amp;quot;func&amp;quot;}.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11906&#34;&gt;#11906&lt;/a&gt;:
Fix regression with &lt;code&gt;pytest.warns&lt;/code&gt;{.interpreted-text
role=&amp;quot;func&amp;quot;} using custom warning subclasses which have more
than one parameter in their [__init__]{.title-ref}.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11907&#34;&gt;#11907&lt;/a&gt;:
Fix a regression in pytest 8.0.0 whereby calling
&lt;code&gt;pytest.skip&lt;/code&gt;{.interpreted-text role=&amp;quot;func&amp;quot;} and
similar control-flow exceptions within a
&lt;code&gt;pytest.warns()&lt;/code&gt;{.interpreted-text role=&amp;quot;func&amp;quot;}
block would get suppressed instead of propagating.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11929&#34;&gt;#11929&lt;/a&gt;:
Fix a regression in pytest 8.0.0 whereby autouse fixtures defined in a
module get ignored by the doctests in the module.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11937&#34;&gt;#11937&lt;/a&gt;:
Fix a regression in pytest 8.0.0 whereby items would be collected in
reverse order in some circumstances.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d7d320a15a1f8dae909e0aa71f20ab5daeaa42d3&#34;&gt;&lt;code&gt;d7d320a&lt;/code&gt;&lt;/a&gt;
Prepare release version 8.0.1&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/93699166dc3d90676b126d2b1615fbd41cf0be4d&#34;&gt;&lt;code&gt;9369916&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11992&#34;&gt;#11992&lt;/a&gt;
from bluetech/backport-11991&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a232abd56cd7ddc0d6dbeefd851c538ec547ab06&#34;&gt;&lt;code&gt;a232abd&lt;/code&gt;&lt;/a&gt;
[8.0.x] recwarn: fix pytest.warns handling of Warnings with multiple
arguments&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/92203d2b78135446510ec70d46452937effcb1d9&#34;&gt;&lt;code&gt;92203d2&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11990&#34;&gt;#11990&lt;/a&gt;
from bluetech/backport-11920&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/f1aa9226ac5b1962fdad442652765d5e589c7137&#34;&gt;&lt;code&gt;f1aa922&lt;/code&gt;&lt;/a&gt;
[8.0.x] recwarn: let base exceptions propagate through
&lt;code&gt;pytest.warns&lt;/code&gt; again&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d86d08156337b40ad0cf6e4bfe38ecfa0e5eb5bd&#34;&gt;&lt;code&gt;d86d081&lt;/code&gt;&lt;/a&gt;
[8.0.x] Added &lt;code&gt;logot&lt;/code&gt; to the plugin list (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11977&#34;&gt;#11977&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/c554c3d200747f9f56b4054619ba4fb6f8910bb5&#34;&gt;&lt;code&gt;c554c3d&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11968&#34;&gt;#11968&lt;/a&gt;
from pytest-dev/backport-11957-to-8.0.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a6851e3459159f94387debf0b357c9b6481a2f48&#34;&gt;&lt;code&gt;a6851e3&lt;/code&gt;&lt;/a&gt;
[8.0.x] main: fix reversed collection order in Session&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/e6f6be3bc9e876f1853fdea68ec49cfc1c4c246d&#34;&gt;&lt;code&gt;e6f6be3&lt;/code&gt;&lt;/a&gt;
[8.0.x] Improve error message when using &lt;a
href=&#34;https://github.com/pytest&#34;&gt;&lt;code&gt;@​pytest&lt;/code&gt;&lt;/a&gt;.fixture twice
(&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11958&#34;&gt;#11958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/23b91d12de9bcbd0ce965bebefcbcc53a588b438&#34;&gt;&lt;code&gt;23b91d1&lt;/code&gt;&lt;/a&gt;
[8.0.x] Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11941&#34;&gt;#11941&lt;/a&gt;
from bluetech/doctest-parsefactories (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11948&#34;&gt;#11948&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/8.0.0...8.0.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=8.0.0&amp;new-version=8.0.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`cd8b9f3`](https://github.com/conijnio/pull-request-codecommit/commit/cd8b9f37d5960f22f70e45abbf72f41d7980df04))

* chore(deps-dev): bump cryptography from 42.0.0 to 42.0.2 (#185)

Bumps [cryptography](https://github.com/pyca/cryptography) from 42.0.0
to 42.0.2.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst&#34;&gt;cryptography&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;42.0.2 - 2024-01-30&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;
* Updated Windows, macOS, and Linux wheels to be compiled with OpenSSL
3.2.1.
* Fixed an issue that prevented the use of Python buffer protocol
objects in
  ``sign`` and ``verify`` methods on asymmetric keys.
* Fixed an issue with incorrect keyword-argument naming with
``EllipticCurvePrivateKey``

:meth:`~cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey.exchange`,
  ``X25519PrivateKey``

:meth:`~cryptography.hazmat.primitives.asymmetric.x25519.X25519PrivateKey.exchange`,
  ``X448PrivateKey``

:meth:`~cryptography.hazmat.primitives.asymmetric.x448.X448PrivateKey.exchange`,
  and ``DHPrivateKey``

:meth:`~cryptography.hazmat.primitives.asymmetric.dh.DHPrivateKey.exchange`.
&lt;p&gt;.. _v42-0-1:&lt;/p&gt;
&lt;p&gt;42.0.1 - 2024-01-24
&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Fixed an issue with incorrect keyword-argument naming with
&lt;code&gt;EllipticCurvePrivateKey&lt;/code&gt;

:meth:&lt;code&gt;~cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey.sign&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;Resolved compatibility issue with loading certain RSA public keys in

:func:&lt;code&gt;~cryptography.hazmat.primitives.serialization.load_pem_public_key&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;.. _v42-0-0:&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/2202123b50de1b8788f909a3e5afe350c56ad81e&#34;&gt;&lt;code&gt;2202123&lt;/code&gt;&lt;/a&gt;
changelog and version bump 42.0.2 (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10268&#34;&gt;#10268&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/f7032bdd409838f67fc2b93343f897fb5f397d80&#34;&gt;&lt;code&gt;f7032bd&lt;/code&gt;&lt;/a&gt;
bump openssl in CI (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10298&#34;&gt;#10298&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10299&#34;&gt;#10299&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/002e886f16d8857151c09b11dc86b35f2ac9aec3&#34;&gt;&lt;code&gt;002e886&lt;/code&gt;&lt;/a&gt;
Fixes &lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10294&#34;&gt;#10294&lt;/a&gt;
-- correct accidental change to exchange kwarg (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10295&#34;&gt;#10295&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10296&#34;&gt;#10296&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/92fa9f2f606caea5d499c825e832be5bac6f0c23&#34;&gt;&lt;code&gt;92fa9f2&lt;/code&gt;&lt;/a&gt;
support bytes-like consistently across our asym sign/verify APIs (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10260&#34;&gt;#10260&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/1&#34;&gt;#1&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/6478f7e28be54b51931277235de01b249ceabd96&#34;&gt;&lt;code&gt;6478f7e&lt;/code&gt;&lt;/a&gt;
explicitly support bytes-like for signature/data in RSA sign/verify (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10259&#34;&gt;#10259&lt;/a&gt;)
...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/4bb8596ae02d95bb054dbcf55e8771379dbe0c19&#34;&gt;&lt;code&gt;4bb8596&lt;/code&gt;&lt;/a&gt;
fix the release script (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10233&#34;&gt;#10233&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10254&#34;&gt;#10254&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/337437dc2e62772bde4ad5544f4b1db9ee7572d9&#34;&gt;&lt;code&gt;337437d&lt;/code&gt;&lt;/a&gt;
42.0.1 bump (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10252&#34;&gt;#10252&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/56255de6b2d1a2d2e502b0275231ca81907f33f1&#34;&gt;&lt;code&gt;56255de&lt;/code&gt;&lt;/a&gt;
allow SPKI RSA keys to be parsed even if they have an incorrect
delimiter (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/1&#34;&gt;#1&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/12f038b38af76e36efe8cef09597010c97647e8f&#34;&gt;&lt;code&gt;12f038b&lt;/code&gt;&lt;/a&gt;
fixes &lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10237&#34;&gt;#10237&lt;/a&gt;
-- correct EC sign parameter name (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10239&#34;&gt;#10239&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10240&#34;&gt;#10240&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/pyca/cryptography/compare/42.0.0...42.0.2&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cryptography&amp;package-manager=pip&amp;previous-version=42.0.0&amp;new-version=42.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/pull-request-codecommit/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`ec2f377`](https://github.com/conijnio/pull-request-codecommit/commit/ec2f3779f9845e8ac5febdbbbabaf0896b245620))

* chore(deps-dev): bump black from 24.1.1 to 24.2.0 (#184)

Bumps [black](https://github.com/psf/black) from 24.1.1 to 24.2.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;24.2.0&lt;/h2&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fixed a bug where comments where mistakenly removed along with
redundant parentheses
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4218&#34;&gt;#4218&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Move the &lt;code&gt;hug_parens_with_braces_and_square_brackets&lt;/code&gt;
feature to the unstable style
due to an outstanding crash and proposed formatting tweaks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4198&#34;&gt;#4198&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fixed a bug where base expressions caused inconsistent formatting of
** in tenary
expression (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4154&#34;&gt;#4154&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Checking for newline before adding one on docstring that is almost
at the line limit
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4185&#34;&gt;#4185&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Remove redundant parentheses in &lt;code&gt;case&lt;/code&gt; statement
&lt;code&gt;if&lt;/code&gt; guards (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4214&#34;&gt;#4214&lt;/a&gt;).&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix issue where &lt;em&gt;Black&lt;/em&gt; would ignore input files in the
presence of symlinks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4222&#34;&gt;#4222&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;em&gt;Black&lt;/em&gt; now ignores &lt;code&gt;pyproject.toml&lt;/code&gt; that is
missing a &lt;code&gt;tool.black&lt;/code&gt; section when
discovering project root and configuration. Since &lt;em&gt;Black&lt;/em&gt;
continues to use version
control as an indicator of project root, this is expected to primarily
change behavior
for users in a monorepo setup (desirably). If you wish to preserve
previous behavior,
simply add an empty &lt;code&gt;[tool.black]&lt;/code&gt; to the previously
discovered &lt;code&gt;pyproject.toml&lt;/code&gt;
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4204&#34;&gt;#4204&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Output&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black will swallow any &lt;code&gt;SyntaxWarning&lt;/code&gt;s or
&lt;code&gt;DeprecationWarning&lt;/code&gt;s produced by the &lt;code&gt;ast&lt;/code&gt;
module when performing equivalence checks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4189&#34;&gt;#4189&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Add a JSONSchema and provide a validate-pyproject entry-point (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4181&#34;&gt;#4181&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;24.2.0&lt;/h2&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fixed a bug where comments where mistakenly removed along with
redundant parentheses
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4218&#34;&gt;#4218&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Move the &lt;code&gt;hug_parens_with_braces_and_square_brackets&lt;/code&gt;
feature to the unstable style
due to an outstanding crash and proposed formatting tweaks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4198&#34;&gt;#4198&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fixed a bug where base expressions caused inconsistent formatting of
** in tenary
expression (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4154&#34;&gt;#4154&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Checking for newline before adding one on docstring that is almost
at the line limit
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4185&#34;&gt;#4185&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Remove redundant parentheses in &lt;code&gt;case&lt;/code&gt; statement
&lt;code&gt;if&lt;/code&gt; guards (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4214&#34;&gt;#4214&lt;/a&gt;).&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix issue where &lt;em&gt;Black&lt;/em&gt; would ignore input files in the
presence of symlinks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4222&#34;&gt;#4222&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;em&gt;Black&lt;/em&gt; now ignores &lt;code&gt;pyproject.toml&lt;/code&gt; that is
missing a &lt;code&gt;tool.black&lt;/code&gt; section when
discovering project root and configuration. Since &lt;em&gt;Black&lt;/em&gt;
continues to use version
control as an indicator of project root, this is expected to primarily
change behavior
for users in a monorepo setup (desirably). If you wish to preserve
previous behavior,
simply add an empty &lt;code&gt;[tool.black]&lt;/code&gt; to the previously
discovered &lt;code&gt;pyproject.toml&lt;/code&gt;
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4204&#34;&gt;#4204&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Output&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black will swallow any &lt;code&gt;SyntaxWarning&lt;/code&gt;s or
&lt;code&gt;DeprecationWarning&lt;/code&gt;s produced by the &lt;code&gt;ast&lt;/code&gt;
module when performing equivalence checks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4189&#34;&gt;#4189&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Add a JSONSchema and provide a validate-pyproject entry-point (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4181&#34;&gt;#4181&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/6fdf8a4af28071ed1d079c01122b34c5d587207a&#34;&gt;&lt;code&gt;6fdf8a4&lt;/code&gt;&lt;/a&gt;
Prepare release 24.2.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4226&#34;&gt;#4226&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/8af439407c051d55f3221cc93795d20bd9af49c9&#34;&gt;&lt;code&gt;8af4394&lt;/code&gt;&lt;/a&gt;
fix: Don&#39;t remove comments along with parens (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4218&#34;&gt;#4218&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/35e97769190d8c8fe94d9ea2d70d7d88b22a2642&#34;&gt;&lt;code&gt;35e9776&lt;/code&gt;&lt;/a&gt;
Bump pre-commit/action from 3.0.0 to 3.0.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4225&#34;&gt;#4225&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/23dfc5b2c3b0694a8c27e58e28439591976aaf94&#34;&gt;&lt;code&gt;23dfc5b&lt;/code&gt;&lt;/a&gt;
Fix ignoring input files for symlink reasons (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4222&#34;&gt;#4222&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/a20100395cf6179a81289452efad1d8e72b19682&#34;&gt;&lt;code&gt;a201003&lt;/code&gt;&lt;/a&gt;
Simplify check for symlinks that resolve outside root (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4221&#34;&gt;#4221&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/dab37a6a1117d690d683121edc4d7c8fb8dd75a7&#34;&gt;&lt;code&gt;dab37a6&lt;/code&gt;&lt;/a&gt;
Remove redundant parentheses in &lt;code&gt;case&lt;/code&gt; statement
&lt;code&gt;if&lt;/code&gt; guards (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4214&#34;&gt;#4214&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/32230e6f5c4bc6bb5c469451e15f3f54d9884b51&#34;&gt;&lt;code&gt;32230e6&lt;/code&gt;&lt;/a&gt;
fix: bug where the doublestar operation had inconsistent formatting. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4154&#34;&gt;#4154&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/7edb50f5a0afc56bb648dc14640ced144366b43a&#34;&gt;&lt;code&gt;7edb50f&lt;/code&gt;&lt;/a&gt;
fix: additional newline added to docstring when the previous line length
is l...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/3e80de3447dee272e9977ab58b1560a669b7b848&#34;&gt;&lt;code&gt;3e80de3&lt;/code&gt;&lt;/a&gt;
Bump furo from 2023.9.10 to 2024.1.29 in /docs (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4211&#34;&gt;#4211&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/a08b480a2f39fb4fc7b210d8b450e33d3879f77d&#34;&gt;&lt;code&gt;a08b480&lt;/code&gt;&lt;/a&gt;
Bump pypa/cibuildwheel from 2.16.4 to 2.16.5 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4212&#34;&gt;#4212&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/24.1.1...24.2.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=24.1.1&amp;new-version=24.2.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`ae5f440`](https://github.com/conijnio/pull-request-codecommit/commit/ae5f44020a7f231577e62d0f2862b0b2089b317a))

* chore(deps-dev): bump twine from 4.0.2 to 5.0.0 (#183) ([`2032a9f`](https://github.com/conijnio/pull-request-codecommit/commit/2032a9f423b253bb69438bad1f712301a87f8283))

* chore(deps-dev): bump twine from 4.0.2 to 5.0.0

Bumps [twine](https://github.com/pypa/twine) from 4.0.2 to 5.0.0.
- [Release notes](https://github.com/pypa/twine/releases)
- [Changelog](https://github.com/pypa/twine/blob/main/docs/changelog.rst)
- [Commits](https://github.com/pypa/twine/compare/4.0.2...5.0.0)

---
updated-dependencies:
- dependency-name: twine
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`257d266`](https://github.com/conijnio/pull-request-codecommit/commit/257d2662a3b5b8b2c225e0cc36bd401a13a5f8ca))

* chore(deps-dev): bump cryptography from 41.0.6 to 42.0.0 (#182)

Bumps [cryptography](https://github.com/pyca/cryptography) from 41.0.6
to 42.0.0.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst&#34;&gt;cryptography&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;42.0.0 - 2024-01-22&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;
* **BACKWARDS INCOMPATIBLE:** Dropped support for LibreSSL &amp;lt; 3.7.
* **BACKWARDS INCOMPATIBLE:** Loading a PKCS7 with no content field
using

:func:`~cryptography.hazmat.primitives.serialization.pkcs7.load_pem_pkcs7_certificates`
  or

:func:`~cryptography.hazmat.primitives.serialization.pkcs7.load_der_pkcs7_certificates`
  will now raise a ``ValueError`` rather than return an empty list.
* Parsing SSH certificates no longer permits malformed critical options
with
  values, as documented in the 41.0.2 release notes.
* Updated Windows, macOS, and Linux wheels to be compiled with OpenSSL
3.2.0.
* Updated the minimum supported Rust version (MSRV) to 1.63.0, from
1.56.0.
* We now publish both ``py37`` and ``py39`` ``abi3`` wheels. This should
resolve some errors relating to initializing a module multiple times per
  process.
* Support
:class:`~cryptography.hazmat.primitives.asymmetric.padding.PSS` for
X.509 certificate signing requests and certificate revocation lists with
the
  keyword-only argument ``rsa_padding`` on the ``sign`` methods for
  :class:`~cryptography.x509.CertificateSigningRequestBuilder` and
  :class:`~cryptography.x509.CertificateRevocationListBuilder`.
* Added support for obtaining X.509 certificate signing request
signature
  algorithm parameters (including PSS) via

:meth:`~cryptography.x509.CertificateSigningRequest.signature_algorithm_parameters`.
* Added support for obtaining X.509 certificate revocation list
signature
  algorithm parameters (including PSS) via

:meth:`~cryptography.x509.CertificateRevocationList.signature_algorithm_parameters`.
* Added ``mgf`` property to
  :class:`~cryptography.hazmat.primitives.asymmetric.padding.PSS`.
* Added ``algorithm`` and ``mgf`` properties to
  :class:`~cryptography.hazmat.primitives.asymmetric.padding.OAEP`.
* Added the following properties that return timezone-aware ``datetime``
objects:
  :meth:`~cryptography.x509.Certificate.not_valid_before_utc`,
  :meth:`~cryptography.x509.Certificate.not_valid_after_utc`,
  :meth:`~cryptography.x509.RevokedCertificate.revocation_date_utc`,
  :meth:`~cryptography.x509.CertificateRevocationList.next_update_utc`,
  :meth:`~cryptography.x509.CertificateRevocationList.last_update_utc`.
These are timezone-aware variants of existing properties that return
naïve
  ``datetime`` objects.
* Deprecated the following properties that return naïve ``datetime``
objects:
  :meth:`~cryptography.x509.Certificate.not_valid_before`,
  :meth:`~cryptography.x509.Certificate.not_valid_after`,
  :meth:`~cryptography.x509.RevokedCertificate.revocation_date`,
  :meth:`~cryptography.x509.CertificateRevocationList.next_update`,
  :meth:`~cryptography.x509.CertificateRevocationList.last_update`
  in favor of the new timezone-aware variants mentioned above.
* Added support for
  :class:`~cryptography.hazmat.primitives.ciphers.algorithms.ChaCha20`
  on LibreSSL.
* Added support for RSA PSS signatures in PKCS7 with
&amp;lt;/tr&amp;gt;&amp;lt;/table&amp;gt; 
&lt;/code&gt;&lt;/pre&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/4e64baf360a3a89bd92582f59344c12b5c0bd3fd&#34;&gt;&lt;code&gt;4e64baf&lt;/code&gt;&lt;/a&gt;
42.0.0 version bump (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10232&#34;&gt;#10232&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/7cb13a3bc91b7537c6231674fb5b0d2132a7edbe&#34;&gt;&lt;code&gt;7cb13a3&lt;/code&gt;&lt;/a&gt;
we&#39;ll ship 3.2.0 for 42 (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/9951&#34;&gt;#9951&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/605c74e41c75edc717f21afaa5e6a0eee9863a10&#34;&gt;&lt;code&gt;605c74e&lt;/code&gt;&lt;/a&gt;
Bump x509-limbo and/or wycheproof in CI (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10231&#34;&gt;#10231&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/97578b98ffc417864e07d0ff9b76c02d2cb4e6da&#34;&gt;&lt;code&gt;97578b9&lt;/code&gt;&lt;/a&gt;
Bump BoringSSL and/or OpenSSL in CI (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10230&#34;&gt;#10230&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/972a7b5896a6047ea43a86db87820ab474d898ff&#34;&gt;&lt;code&gt;972a7b5&lt;/code&gt;&lt;/a&gt;
verification: add test_verify_tz_aware (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10229&#34;&gt;#10229&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/41daf2d86dd9bf18081802fa5d851a7953810786&#34;&gt;&lt;code&gt;41daf2d&lt;/code&gt;&lt;/a&gt;
Migrate PKCS7 backend to Rust (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10228&#34;&gt;#10228&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/d54093e62e7e68c02efbb4d6a09162ddb39bf72f&#34;&gt;&lt;code&gt;d54093e&lt;/code&gt;&lt;/a&gt;
Remove some skips in tests that aren&#39;t needed anymore (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10223&#34;&gt;#10223&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/71929bd91f34213b9f4a3a0a493c218c35fa25eb&#34;&gt;&lt;code&gt;71929bd&lt;/code&gt;&lt;/a&gt;
Remove binding that&#39;s not used anymore (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10224&#34;&gt;#10224&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/7ea4b89cea553ce0f641ed29e1ce2e3e34278f1d&#34;&gt;&lt;code&gt;7ea4b89&lt;/code&gt;&lt;/a&gt;
fixed formatting in changelog (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10225&#34;&gt;#10225&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/410f4a1ee4cbf46fe7e969bb48fccf261f74bbcd&#34;&gt;&lt;code&gt;410f4a1&lt;/code&gt;&lt;/a&gt;
Allow brainpool on libressl (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10222&#34;&gt;#10222&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pyca/cryptography/compare/41.0.6...42.0.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cryptography&amp;package-manager=pip&amp;previous-version=41.0.6&amp;new-version=42.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/pull-request-codecommit/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`3a39473`](https://github.com/conijnio/pull-request-codecommit/commit/3a394736ccd74fa3afad2df778e1dd6b300b1745))

* chore(deps-dev): bump black from 23.12.1 to 24.1.1 (#181)

Bumps [black](https://github.com/psf/black) from 23.12.1 to 24.1.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;24.1.1&lt;/h2&gt;
&lt;p&gt;Bugfix release to fix a bug that made Black unusable on certain file
systems
with strict limits on path length.&lt;/p&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Consistently add trailing comma on typed parameters (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4164&#34;&gt;#4164&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Shorten the length of the name of the cache file to fix crashes on
file systems that
do not support long paths (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4176&#34;&gt;#4176&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;24.1.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;p&gt;This release introduces the new 2024 stable style (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4106&#34;&gt;#4106&lt;/a&gt;),
stabilizing the following
changes:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Add parentheses around &lt;code&gt;if&lt;/code&gt;-&lt;code&gt;else&lt;/code&gt; expressions
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/2278&#34;&gt;#2278&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Dummy class and function implementations consisting only of
&lt;code&gt;...&lt;/code&gt; are formatted more
compactly (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3796&#34;&gt;#3796&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;If an assignment statement is too long, we now prefer splitting on
the right-hand side
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3368&#34;&gt;#3368&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Hex codes in Unicode escape sequences are now standardized to
lowercase (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/2916&#34;&gt;#2916&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty first lines at the beginning of most blocks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;, &lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4061&#34;&gt;#4061&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add parentheses around long type annotations (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3899&#34;&gt;#3899&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Enforce newline after module docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;, &lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4028&#34;&gt;#4028&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix incorrect magic trailing comma handling in return types (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3916&#34;&gt;#3916&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Remove blank lines before class docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3692&#34;&gt;#3692&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Wrap multiple context managers in parentheses if combined in a
single &lt;code&gt;with&lt;/code&gt; statement
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3489&#34;&gt;#3489&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix bug in line length calculations for power operations (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3942&#34;&gt;#3942&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add trailing commas to collection literals even if there&#39;s a comment
after the last
entry (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3393&#34;&gt;#3393&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;When using &lt;code&gt;--skip-magic-trailing-comma&lt;/code&gt; or
&lt;code&gt;-C&lt;/code&gt;, trailing commas are stripped from
subscript expressions with more than 1 element (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3209&#34;&gt;#3209&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add extra blank lines in stubs in a few cases (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3564&#34;&gt;#3564&lt;/a&gt;, &lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3862&#34;&gt;#3862&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Accept raw strings as docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Split long lines in case blocks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Stop removing spaces from walrus operators within subscripts (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3823&#34;&gt;#3823&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix incorrect formatting of certain async statements (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3609&#34;&gt;#3609&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow combining &lt;code&gt;# fmt: skip&lt;/code&gt; with other comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3959&#34;&gt;#3959&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;There are already a few improvements in the &lt;code&gt;--preview&lt;/code&gt;
style, which are slated for the
2025 stable style. Try them out and
&lt;a href=&#34;https://github.com/psf/black/issues&#34;&gt;share your feedback&lt;/a&gt;.
In the past, the preview
style has included some features that we were not able to stabilize.
This year, we&#39;re&lt;/p&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;24.1.1&lt;/h2&gt;
&lt;p&gt;Bugfix release to fix a bug that made Black unusable on certain file
systems with strict
limits on path length.&lt;/p&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Consistently add trailing comma on typed parameters (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4164&#34;&gt;#4164&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Shorten the length of the name of the cache file to fix crashes on
file systems that
do not support long paths (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4176&#34;&gt;#4176&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;24.1.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;p&gt;This release introduces the new 2024 stable style (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4106&#34;&gt;#4106&lt;/a&gt;),
stabilizing the following
changes:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Add parentheses around &lt;code&gt;if&lt;/code&gt;-&lt;code&gt;else&lt;/code&gt; expressions
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/2278&#34;&gt;#2278&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Dummy class and function implementations consisting only of
&lt;code&gt;...&lt;/code&gt; are formatted more
compactly (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3796&#34;&gt;#3796&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;If an assignment statement is too long, we now prefer splitting on
the right-hand side
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3368&#34;&gt;#3368&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Hex codes in Unicode escape sequences are now standardized to
lowercase (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/2916&#34;&gt;#2916&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty first lines at the beginning of most blocks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;, &lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4061&#34;&gt;#4061&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add parentheses around long type annotations (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3899&#34;&gt;#3899&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Enforce newline after module docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;, &lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4028&#34;&gt;#4028&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix incorrect magic trailing comma handling in return types (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3916&#34;&gt;#3916&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Remove blank lines before class docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3692&#34;&gt;#3692&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Wrap multiple context managers in parentheses if combined in a
single &lt;code&gt;with&lt;/code&gt; statement
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3489&#34;&gt;#3489&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix bug in line length calculations for power operations (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3942&#34;&gt;#3942&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add trailing commas to collection literals even if there&#39;s a comment
after the last
entry (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3393&#34;&gt;#3393&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;When using &lt;code&gt;--skip-magic-trailing-comma&lt;/code&gt; or
&lt;code&gt;-C&lt;/code&gt;, trailing commas are stripped from
subscript expressions with more than 1 element (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3209&#34;&gt;#3209&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add extra blank lines in stubs in a few cases (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3564&#34;&gt;#3564&lt;/a&gt;, &lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3862&#34;&gt;#3862&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Accept raw strings as docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Split long lines in case blocks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Stop removing spaces from walrus operators within subscripts (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3823&#34;&gt;#3823&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix incorrect formatting of certain async statements (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3609&#34;&gt;#3609&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow combining &lt;code&gt;# fmt: skip&lt;/code&gt; with other comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3959&#34;&gt;#3959&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;There are already a few improvements in the &lt;code&gt;--preview&lt;/code&gt;
style, which are slated for the
2025 stable style. Try them out and
&lt;a href=&#34;https://github.com/psf/black/issues&#34;&gt;share your feedback&lt;/a&gt;.
In the past, the preview
style has included some features that we were not able to stabilize.
This year, we&#39;re&lt;/p&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/e026c93888f91a47a9c9f4e029f3eb07d96375e6&#34;&gt;&lt;code&gt;e026c93&lt;/code&gt;&lt;/a&gt;
Prepare release 24.1.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4186&#34;&gt;#4186&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/79fc1158a98281dac798feb14b8fddb4051e4a42&#34;&gt;&lt;code&gt;79fc115&lt;/code&gt;&lt;/a&gt;
chore: ignore node_modules (produced by a pre-commit check) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4184&#34;&gt;#4184&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/8bf04549ffd276a1bad6eb110e66e6557ee630d9&#34;&gt;&lt;code&gt;8bf0454&lt;/code&gt;&lt;/a&gt;
Consistently add trailing comma on typed parameters (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4164&#34;&gt;#4164&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/1607e9ab20ad550cf940482d0d361ca31fc03189&#34;&gt;&lt;code&gt;1607e9a&lt;/code&gt;&lt;/a&gt;
Fix missing space in option description (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4182&#34;&gt;#4182&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ed770ba4dd50c419148a0fca2b43937a7447e1f9&#34;&gt;&lt;code&gt;ed770ba&lt;/code&gt;&lt;/a&gt;
Fix cache file length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4176&#34;&gt;#4176&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/659c29a41c7c686687aef21f57b95bcfa236b03b&#34;&gt;&lt;code&gt;659c29a&lt;/code&gt;&lt;/a&gt;
New changelog&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/0e6e46b9eb45f5a22062fe84c2c2ff46bd0d738e&#34;&gt;&lt;code&gt;0e6e46b&lt;/code&gt;&lt;/a&gt;
Prepare release 24.1.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4170&#34;&gt;#4170&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/4f47cac1925a2232892ceae438e2c62f81517714&#34;&gt;&lt;code&gt;4f47cac&lt;/code&gt;&lt;/a&gt;
Add --unstable flag (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4096&#34;&gt;#4096&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/bccec8adfbed2bbc24c0859e8758d5e7809d42b7&#34;&gt;&lt;code&gt;bccec8a&lt;/code&gt;&lt;/a&gt;
Show warning on invalid toml configuration (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4165&#34;&gt;#4165&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/7d789469ed947022f183962b823f5862511272ac&#34;&gt;&lt;code&gt;7d78946&lt;/code&gt;&lt;/a&gt;
Describe 2024 module docstring more accurately (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4168&#34;&gt;#4168&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/23.12.1...24.1.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.12.1&amp;new-version=24.1.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt; ([`bfa899d`](https://github.com/conijnio/pull-request-codecommit/commit/bfa899d2d1b479357de2db822e23d4f2b47d790f))

* chore(deps-dev): bump black from 23.12.1 to 24.1.1

Bumps [black](https://github.com/psf/black) from 23.12.1 to 24.1.1.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.12.1...24.1.1)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b715dfc`](https://github.com/conijnio/pull-request-codecommit/commit/b715dfcfc2c86d9684366556f225866f1a12189d))

* chore(deps-dev): bump pytest from 7.4.4 to 8.0.0 (#180)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.4 to
8.0.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;pytest 8.0.0 (2024-01-27)&lt;/h2&gt;
&lt;p&gt;See &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases/tag/8.0.0rc1&#34;&gt;8.0.0rc1&lt;/a&gt;
and &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases/tag/8.0.0rc2&#34;&gt;8.0.0rc2&lt;/a&gt;
for the full changes since pytest 7.4!&lt;/p&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11842&#34;&gt;#11842&lt;/a&gt;:
Properly escape the &lt;code&gt;reason&lt;/code&gt; of a &lt;code&gt;skip
&amp;lt;pytest.mark.skip ref&amp;gt;&lt;/code&gt;{.interpreted-text
role=&amp;quot;ref&amp;quot;} mark when writing JUnit XML files.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11861&#34;&gt;#11861&lt;/a&gt;:
Avoid microsecond exceeds &lt;code&gt;1_000_000&lt;/code&gt; when using
&lt;code&gt;log-date-format&lt;/code&gt; with &lt;code&gt;%f&lt;/code&gt; specifier, which might
cause the test suite to crash.&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;8.0.0rc2&lt;/h2&gt;
&lt;h1&gt;pytest 8.0.0rc2 (2024-01-17)&lt;/h1&gt;
&lt;h2&gt;Improvements&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11233&#34;&gt;#11233&lt;/a&gt;:
Improvements to &lt;code&gt;-r&lt;/code&gt; for xfailures and xpasses:
&lt;ul&gt;
&lt;li&gt;Report tracebacks for xfailures when &lt;code&gt;-rx&lt;/code&gt; is set.&lt;/li&gt;
&lt;li&gt;Report captured output for xpasses when &lt;code&gt;-rX&lt;/code&gt; is
set.&lt;/li&gt;
&lt;li&gt;For xpasses, add &lt;code&gt;-&lt;/code&gt; in summary between test name and
reason, to match how xfail is displayed.&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11825&#34;&gt;#11825&lt;/a&gt;:
The &lt;code&gt;pytest_plugin_registered&lt;/code&gt;{.interpreted-text
role=&amp;quot;hook&amp;quot;} hook has a new &lt;code&gt;plugin_name&lt;/code&gt; parameter
containing the name by which &lt;code&gt;plugin&lt;/code&gt; is registered.&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11706&#34;&gt;#11706&lt;/a&gt;:
Fix reporting of teardown errors in higher-scoped fixtures when using
[--maxfail]{.title-ref} or [--stepwise]{.title-ref}.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11758&#34;&gt;#11758&lt;/a&gt;:
Fixed &lt;code&gt;IndexError: string index out of range&lt;/code&gt; crash in
&lt;code&gt;if highlighted[-1] == &amp;quot;\n&amp;quot; and source[-1] !=
&amp;quot;\n&amp;quot;&lt;/code&gt;.
This bug was introduced in pytest 8.0.0rc1.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/9765&#34;&gt;#9765&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11816&#34;&gt;#11816&lt;/a&gt;:
Fixed a frustrating bug that afflicted some users with the only error
being &lt;code&gt;assert mod not in mods&lt;/code&gt;. The issue was caused by the
fact that &lt;code&gt;str(Path(mod))&lt;/code&gt; and &lt;code&gt;mod.__file__&lt;/code&gt;
don&#39;t necessarily produce the same string, and was being erroneously
used interchangably in some places in the code.&lt;/p&gt;
&lt;p&gt;This fix also broke the internal API of
&lt;code&gt;PytestPluginManager.consider_conftest&lt;/code&gt; by introducing a new
parameter -- we mention this in case it is being used by external code,
even if marked as &lt;em&gt;private&lt;/em&gt;.&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;pytest 8.0.0rc1 (2023-12-30)&lt;/h2&gt;
&lt;p&gt;See &lt;a
href=&#34;https://docs.pytest.org/en/latest/changelog.html#pytest-8-0-0rc1-2023-12-30&#34;&gt;https://docs.pytest.org/en/latest/changelog.html#pytest-8-0-0rc1-2023-12-30&lt;/a&gt;
for the rendered changelog.&lt;/p&gt;
&lt;h2&gt;Breaking Changes&lt;/h2&gt;
&lt;h3&gt;Old Deprecations Are Now Errors&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/7363&#34;&gt;#7363&lt;/a&gt;:
&lt;strong&gt;PytestRemovedIn8Warning deprecation warnings are now errors by
default.&lt;/strong&gt;&lt;/p&gt;
&lt;p&gt;Following our plan to remove deprecated features with as little
disruption as possible, all warnings of type
&lt;code&gt;PytestRemovedIn8Warning&lt;/code&gt; now generate errors instead of
warning messages by default.&lt;/p&gt;
&lt;p&gt;&lt;strong&gt;The affected features will be effectively removed in pytest
8.1&lt;/strong&gt;, so please consult the
&lt;code&gt;deprecations&lt;/code&gt;{.interpreted-text role=&amp;quot;ref&amp;quot;}
section in the docs for directions on how to update existing code.&lt;/p&gt;
&lt;p&gt;In the pytest &lt;code&gt;8.0.X&lt;/code&gt; series, it is possible to change the
errors back into warnings as a stopgap measure by adding this to your
&lt;code&gt;pytest.ini&lt;/code&gt; file:&lt;/p&gt;
&lt;pre lang=&#34;ini&#34;&gt;&lt;code&gt;[pytest]
&lt;/code&gt;&lt;/pre&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/478f8233bca8147445f0c5129f04ada892cc6c91&#34;&gt;&lt;code&gt;478f823&lt;/code&gt;&lt;/a&gt;
Prepare release version 8.0.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/608590097a6542768099dd371b84d8b37a1990da&#34;&gt;&lt;code&gt;6085900&lt;/code&gt;&lt;/a&gt;
[8.0.x] fix: avoid rounding microsecond to &lt;code&gt;1_000_000&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11863&#34;&gt;#11863&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/3b41c65c81d649d962be5ec469f44104b8d09748&#34;&gt;&lt;code&gt;3b41c65&lt;/code&gt;&lt;/a&gt;
[8.0.x] Escape skip reason in junitxml (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11845&#34;&gt;#11845&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/747072ad26f2443dc8a62eb88db8cbf56fa95470&#34;&gt;&lt;code&gt;747072a&lt;/code&gt;&lt;/a&gt;
[8.0.x] Update docstring of scripts/generate-gh-release-notes.py (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11768&#34;&gt;#11768&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/011a475baf6e1d0e9ec30c5996d9cbcbe7c95475&#34;&gt;&lt;code&gt;011a475&lt;/code&gt;&lt;/a&gt;
Properly attach packages to the GH release notes (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11839&#34;&gt;#11839&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11840&#34;&gt;#11840&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/97960bdd148972b2f26bd9b336163e590bbc4c6b&#34;&gt;&lt;code&gt;97960bd&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11835&#34;&gt;#11835&lt;/a&gt;
from pytest-dev/release-8.0.0rc2&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/6be0a3cbf7e014834610139421a0d9804d4a3eae&#34;&gt;&lt;code&gt;6be0a3c&lt;/code&gt;&lt;/a&gt;
Prepare release version 8.0.0rc2&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/44ffe071658f5ac609fe8d3b967e8dba93abc819&#34;&gt;&lt;code&gt;44ffe07&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11837&#34;&gt;#11837&lt;/a&gt;
from pytest-dev/backport-11836-to-8.0.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/14ecb049732bed4dc913e2da55c616882432c978&#34;&gt;&lt;code&gt;14ecb04&lt;/code&gt;&lt;/a&gt;
[8.0.x] testing: temporarily disable test due to hypothesis issue&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/41c8dabee3c40a5d363bf03a3ca2370ee27cbcd0&#34;&gt;&lt;code&gt;41c8dab&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11831&#34;&gt;#11831&lt;/a&gt;
from bluetech/backport-11825-to-8.0.x&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/7.4.4...8.0.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=7.4.4&amp;new-version=8.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt; ([`a80f502`](https://github.com/conijnio/pull-request-codecommit/commit/a80f5026e80a36ae7e1a780634091949e01e96d2))

* chore(deps-dev): bump pytest from 7.4.4 to 8.0.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.4 to 8.0.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.4.4...8.0.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6e82479`](https://github.com/conijnio/pull-request-codecommit/commit/6e82479c48d4e9210ec11ff0ca79e35d6c6cff38))

* chore(deps-dev): bump pytest from 7.4.3 to 7.4.4 (#179)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.3 to
7.4.4.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;pytest 7.4.4 (2023-12-31)&lt;/h2&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11140&#34;&gt;#11140&lt;/a&gt;:
Fix non-string constants at the top of file being detected as docstrings
on Python&amp;gt;=3.8.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11572&#34;&gt;#11572&lt;/a&gt;:
Handle an edge case where &lt;code&gt;sys.stderr&lt;/code&gt;{.interpreted-text
role=&amp;quot;data&amp;quot;} and &lt;code&gt;sys.__stderr__&lt;/code&gt;{.interpreted-text
role=&amp;quot;data&amp;quot;} might already be closed when
&lt;code&gt;faulthandler&lt;/code&gt;{.interpreted-text role=&amp;quot;ref&amp;quot;} is
tearing down.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11710&#34;&gt;#11710&lt;/a&gt;:
Fixed tracebacks from collection errors not getting pruned.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/7966&#34;&gt;#7966&lt;/a&gt;:
Removed unhelpful error message from assertion rewrite mechanism when
exceptions are raised in &lt;code&gt;__iter__&lt;/code&gt; methods. Now they are
treated un-iterable instead.&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Improved Documentation&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11091&#34;&gt;#11091&lt;/a&gt;:
Updated documentation to refer to hyphenated options: replaced
&lt;code&gt;--junitxml&lt;/code&gt; with &lt;code&gt;--junit-xml&lt;/code&gt; and
&lt;code&gt;--collectonly&lt;/code&gt; with &lt;code&gt;--collect-only&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/33f694f4b30c5c502f21f81cb8ab907b12ad2f65&#34;&gt;&lt;code&gt;33f694f&lt;/code&gt;&lt;/a&gt;
Prepare release version 7.4.4&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/76c107c463afcaddf74ca48252614728c6829ea7&#34;&gt;&lt;code&gt;76c107c&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11751&#34;&gt;#11751&lt;/a&gt;
from bluetech/backport-11143-to-7.4.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/531d76daa4a871df5b2a46cae132851c29abf027&#34;&gt;&lt;code&gt;531d76d&lt;/code&gt;&lt;/a&gt;
[7.4.x] Improve reporting from &lt;strong&gt;iter&lt;/strong&gt; exceptions (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11749&#34;&gt;#11749&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a0f58fa9e7f9b09b212ed491464be5df9b80fc0b&#34;&gt;&lt;code&gt;a0f58fa&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11143&#34;&gt;#11143&lt;/a&gt;
from tushar-deepsource/patch-1&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/b1f3387d42571090ee4a35ec1945765b7f2ffae8&#34;&gt;&lt;code&gt;b1f3387&lt;/code&gt;&lt;/a&gt;
[7.4.x] &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11091&#34;&gt;#11091&lt;/a&gt;:
documentation should use hypthonated properties (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11750&#34;&gt;#11750&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/2cdd619bf49ee7c5306dc70dcbf71090839ea985&#34;&gt;&lt;code&gt;2cdd619&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11747&#34;&gt;#11747&lt;/a&gt;
from pytest-dev/backport-11711-to-7.4.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d06c05bd23ea6af8e07fd944e56c58b64375b724&#34;&gt;&lt;code&gt;d06c05b&lt;/code&gt;&lt;/a&gt;
[7.4.x] nodes: fix tracebacks from collection errors are not getting
pruned&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/5582bfcddf78929f7979c5023b167b333e1c2dd9&#34;&gt;&lt;code&gt;5582bfc&lt;/code&gt;&lt;/a&gt;
[7.4.x] Improves clarity in Sphinx documentation for function signature.
(&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11&#34;&gt;#11&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/13024efd7afdbae80ce70d27295d9bbe62670cb8&#34;&gt;&lt;code&gt;13024ef&lt;/code&gt;&lt;/a&gt;
[7.4.x] Fix for operation on closed file in faulthandler teardown (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11631&#34;&gt;#11631&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a40dacf6577ae990740e10572582538dfaf357b6&#34;&gt;&lt;code&gt;a40dacf&lt;/code&gt;&lt;/a&gt;
[7.4.x] XFAIL TestLocalPath.test_make_numbered_dir_multiprocess_safe (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11616&#34;&gt;#11616&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/7.4.3...7.4.4&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=7.4.3&amp;new-version=7.4.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`b7aff00`](https://github.com/conijnio/pull-request-codecommit/commit/b7aff001507c95f873c1382b856c612a4d69236b))

* chore(deps-dev): bump black from 23.12.0 to 23.12.1 (#178)

Bumps [black](https://github.com/psf/black) from 23.12.0 to 23.12.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.1&lt;/h2&gt;
&lt;p&gt;Fixed a bug that included dependencies from the d extra by default
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4108&#34;&gt;#4108&lt;/a&gt;)&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.1&lt;/h2&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fixed a bug that included dependencies from the &lt;code&gt;d&lt;/code&gt; extra
by default (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4108&#34;&gt;#4108&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ec91a2be3c44d88e1a3960a4937ad6ed3b63464e&#34;&gt;&lt;code&gt;ec91a2b&lt;/code&gt;&lt;/a&gt;
Prepare release 23.12.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4124&#34;&gt;#4124&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/8fec1c30855890cc9cfce5ae6d633a1c1a21d724&#34;&gt;&lt;code&gt;8fec1c3&lt;/code&gt;&lt;/a&gt;
Adds paren to deps for hidden extra constraint (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4108&#34;&gt;#4108&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/35ce37ded7bd8fdd3950af19e7c11f311ee7b8d8&#34;&gt;&lt;code&gt;35ce37d&lt;/code&gt;&lt;/a&gt;
Add new changelog template&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/psf/black/compare/23.12.0...23.12.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.12.0&amp;new-version=23.12.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`686ff6e`](https://github.com/conijnio/pull-request-codecommit/commit/686ff6e446ecf383ea14fd09c46bfd2fef1f78a2))

* chore(deps-dev): bump mypy from 1.7.1 to 1.8.0 (#177)

Bumps [mypy](https://github.com/python/mypy) from 1.7.1 to 1.8.0.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python/mypy/blob/master/CHANGELOG.md&#34;&gt;mypy&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;Mypy Release Notes&lt;/h1&gt;
&lt;h2&gt;Next release&lt;/h2&gt;
&lt;h2&gt;Mypy 1.8&lt;/h2&gt;
&lt;p&gt;We’ve just uploaded mypy 1.8 to the Python Package Index (&lt;a
href=&#34;https://pypi.org/project/mypy/&#34;&gt;PyPI&lt;/a&gt;). Mypy is a static type
checker for Python. This release includes new features, performance
improvements and bug fixes. You can install it as follows:&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;python3 -m pip install -U mypy
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;You can read the full documentation for this release on &lt;a
href=&#34;http://mypy.readthedocs.io&#34;&gt;Read the Docs&lt;/a&gt;.&lt;/p&gt;
&lt;h4&gt;Type-checking Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Do not intersect types in isinstance checks if at least one is final
(Christoph Tyralla, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16330&#34;&gt;16330&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Detect that &lt;code&gt;@final&lt;/code&gt; class without &lt;code&gt;__bool__&lt;/code&gt;
cannot have falsey instances (Ilya Priven, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16566&#34;&gt;16566&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Do not allow &lt;code&gt;TypedDict&lt;/code&gt; classes with extra keywords
(Nikita Sobolev, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16438&#34;&gt;16438&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Do not allow class-level keywords for &lt;code&gt;NamedTuple&lt;/code&gt;
(Nikita Sobolev, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16526&#34;&gt;16526&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Make imprecise constraints handling more robust (Ivan Levkivskyi, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16502&#34;&gt;16502&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix strict-optional in extending generic TypedDict (Ivan Levkivskyi,
PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16398&#34;&gt;16398&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow type ignores of PEP 695 constructs (Shantanu, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16608&#34;&gt;16608&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Enable &lt;code&gt;type_check_only&lt;/code&gt; support for
&lt;code&gt;TypedDict&lt;/code&gt; and &lt;code&gt;NamedTuple&lt;/code&gt; (Nikita Sobolev, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16469&#34;&gt;16469&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Performance Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Add fast path to analyzing special form assignments (Jukka
Lehtosalo, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16561&#34;&gt;16561&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Improvements to Error Reporting&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Don&#39;t show documentation links for plugin error codes (Ivan
Levkivskyi, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16383&#34;&gt;16383&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Improve error messages for &lt;code&gt;super&lt;/code&gt; checks and add more
tests (Nikita Sobolev, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16393&#34;&gt;16393&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add error code for mutable covariant override (Ivan Levkivskyi, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16399&#34;&gt;16399&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Stubgen Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Preserve simple defaults in function signatures (Ali Hamdan, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/15355&#34;&gt;15355&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Include &lt;code&gt;__all__&lt;/code&gt; in output (Jelle Zijlstra, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16356&#34;&gt;16356&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix stubgen regressions with pybind11 and mypy 1.7 (Chad Dombrova,
PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16504&#34;&gt;16504&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Stubtest Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Improve handling of unrepresentable defaults (Jelle Zijlstra, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16433&#34;&gt;16433&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Print more helpful errors if a function is missing from stub (Alex
Waygood, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16517&#34;&gt;16517&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Support &lt;code&gt;@type_check_only&lt;/code&gt; decorator (Nikita Sobolev, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16422&#34;&gt;16422&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Warn about missing &lt;code&gt;__del__&lt;/code&gt; (Shantanu, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16456&#34;&gt;16456&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crashes with some uses of &lt;code&gt;final&lt;/code&gt; and
&lt;code&gt;deprecated&lt;/code&gt; (Shantanu, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16457&#34;&gt;16457&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Fixes to Crashes&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Fix crash with type alias to &lt;code&gt;Callable[[Unpack[Tuple[Any,
...]]], Any]&lt;/code&gt; (Alex Waygood, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16541&#34;&gt;16541&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on TypeGuard in &lt;code&gt;__call__&lt;/code&gt; (Ivan Levkivskyi, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16516&#34;&gt;16516&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on invalid enum in method (Ivan Levkivskyi, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16511&#34;&gt;16511&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on unimported Any in TypedDict (Ivan Levkivskyi, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16510&#34;&gt;16510&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Documentation Updates&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Update soft-error-limit default value to -1 (Sveinung Gundersen, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16542&#34;&gt;16542&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/3b467509ee29b8f274c035d78a1c241a781eb311&#34;&gt;&lt;code&gt;3b46750&lt;/code&gt;&lt;/a&gt;
remove +dev suffix from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c9bc833bc8a64e3517a6843bbf982a37ee54f893&#34;&gt;&lt;code&gt;c9bc833&lt;/code&gt;&lt;/a&gt;
Fix tests broken by hatchling (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16655&#34;&gt;#16655&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/60d30e36c49a2753de2d71f7dd50f5143bafd307&#34;&gt;&lt;code&gt;60d30e3&lt;/code&gt;&lt;/a&gt;
Fix crash with type alias to &lt;code&gt;Callable[[Unpack[Tuple[Any, ...]]],
Any]&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16541&#34;&gt;#16541&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f53f4222bbb12d49612657a48b4f2b77e15402fd&#34;&gt;&lt;code&gt;f53f422&lt;/code&gt;&lt;/a&gt;
Allow type ignores of PEP 695 constructs (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16608&#34;&gt;#16608&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/7c33e7c03444ae748b82163e7b4e1666dfaf94c7&#34;&gt;&lt;code&gt;7c33e7c&lt;/code&gt;&lt;/a&gt;
&lt;a href=&#34;https://github.com/final&#34;&gt;&lt;code&gt;@​final&lt;/code&gt;&lt;/a&gt; class
without &lt;strong&gt;bool&lt;/strong&gt; cannot have falsey instances (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16566&#34;&gt;#16566&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c224da5c7c414f92ded4b7816d16d5dd4ed32193&#34;&gt;&lt;code&gt;c224da5&lt;/code&gt;&lt;/a&gt;
Do not intersect types in isinstance checks if at least one is final (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16330&#34;&gt;#16330&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/d54cc35a93b1f1bda8f837e0f3ae6f964a1c7feb&#34;&gt;&lt;code&gt;d54cc35&lt;/code&gt;&lt;/a&gt;
Change example in test cases with no stubs available (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16513&#34;&gt;#16513&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/eb1ee973778e3cf719948e1653db9760ea49405d&#34;&gt;&lt;code&gt;eb1ee97&lt;/code&gt;&lt;/a&gt;
Update hashes in &lt;code&gt;sync-typeshed.py&lt;/code&gt; following recent typeshed
sync (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16600&#34;&gt;#16600&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/344298e3a7b1a299092c684c11c28e9f4dc44dd9&#34;&gt;&lt;code&gt;344298e&lt;/code&gt;&lt;/a&gt;
Revert use of &lt;code&gt;ParamSpec&lt;/code&gt; for
&lt;code&gt;functools.wraps&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/3e5d813372e4fc1899319f31425bfc11c27fddb3&#34;&gt;&lt;code&gt;3e5d813&lt;/code&gt;&lt;/a&gt;
Revert typeshed ctypes change&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.7.1...v1.8.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.7.1&amp;new-version=1.8.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`1716c96`](https://github.com/conijnio/pull-request-codecommit/commit/1716c96511e12eea507bc4f530e4c763314863b5))

* chore(deps-dev): bump black from 23.11.0 to 23.12.0 (#176)

Bumps [black](https://github.com/psf/black) from 23.11.0 to 23.12.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;p&gt;It&#39;s almost 2024, which means it&#39;s time for a new edition of
&lt;em&gt;Black&lt;/em&gt;&#39;s stable style!
Together with this release, we&#39;ll put out an alpha release 24.1a1
showcasing the draft
2024 stable style, which we&#39;ll finalize in the January release. Please
try it out and
&lt;a href=&#34;https://redirect.github.com/psf/black/issues/4042&#34;&gt;share your
feedback&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;This release (23.12.0) will still produce the 2023 style. Most but
not all of the
changes in &lt;code&gt;--preview&lt;/code&gt; mode will be in the 2024 stable
style.&lt;/p&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where &lt;code&gt;# fmt: off&lt;/code&gt; automatically dedents when
used with the &lt;code&gt;--line-ranges&lt;/code&gt;
option, even when it is not within the specified line range. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4084&#34;&gt;#4084&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix feature detection for parenthesized context managers (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4104&#34;&gt;#4104&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Prefer more equal signs before a break when splitting chained
assignments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4010&#34;&gt;#4010&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Standalone form feed characters at the module level are no longer
removed (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4021&#34;&gt;#4021&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional cases of immediately nested tuples, lists, and
dictionaries are now
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4012&#34;&gt;#4012&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty lines at the beginning of all blocks, except immediately
before a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4060&#34;&gt;#4060&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash in preview mode when using a short
&lt;code&gt;--line-length&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4086&#34;&gt;#4086&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep suites consisting of only an ellipsis on their own lines if
they are not
functions or class definitions (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4066&#34;&gt;#4066&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4103&#34;&gt;#4103&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;--line-ranges&lt;/code&gt; now skips &lt;em&gt;Black&lt;/em&gt;&#39;s internal
stability check in &lt;code&gt;--safe&lt;/code&gt; mode. This
avoids a crash on rare inputs that have many unformatted same-content
lines. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4034&#34;&gt;#4034&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Upgrade to mypy 1.7.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4049&#34;&gt;#4049&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4069&#34;&gt;#4069&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Faster compiled wheels are now available for CPython 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4070&#34;&gt;#4070&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Enable 3.12 CI (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4035&#34;&gt;#4035&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images in parallel (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4054&#34;&gt;#4054&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images with 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4055&#34;&gt;#4055&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;p&gt;It&#39;s almost 2024, which means it&#39;s time for a new edition of
&lt;em&gt;Black&lt;/em&gt;&#39;s stable style!
Together with this release, we&#39;ll put out an alpha release 24.1a1
showcasing the draft
2024 stable style, which we&#39;ll finalize in the January release. Please
try it out and
&lt;a href=&#34;https://redirect.github.com/psf/black/issues/4042&#34;&gt;share your
feedback&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;This release (23.12.0) will still produce the 2023 style. Most but
not all of the
changes in &lt;code&gt;--preview&lt;/code&gt; mode will be in the 2024 stable
style.&lt;/p&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where &lt;code&gt;# fmt: off&lt;/code&gt; automatically dedents when
used with the &lt;code&gt;--line-ranges&lt;/code&gt;
option, even when it is not within the specified line range. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4084&#34;&gt;#4084&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix feature detection for parenthesized context managers (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4104&#34;&gt;#4104&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Prefer more equal signs before a break when splitting chained
assignments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4010&#34;&gt;#4010&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Standalone form feed characters at the module level are no longer
removed (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4021&#34;&gt;#4021&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional cases of immediately nested tuples, lists, and
dictionaries are now
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4012&#34;&gt;#4012&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty lines at the beginning of all blocks, except immediately
before a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4060&#34;&gt;#4060&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash in preview mode when using a short
&lt;code&gt;--line-length&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4086&#34;&gt;#4086&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep suites consisting of only an ellipsis on their own lines if
they are not
functions or class definitions (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4066&#34;&gt;#4066&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4103&#34;&gt;#4103&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;--line-ranges&lt;/code&gt; now skips &lt;em&gt;Black&lt;/em&gt;&#39;s internal
stability check in &lt;code&gt;--safe&lt;/code&gt; mode. This
avoids a crash on rare inputs that have many unformatted same-content
lines. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4034&#34;&gt;#4034&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Upgrade to mypy 1.7.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4049&#34;&gt;#4049&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4069&#34;&gt;#4069&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Faster compiled wheels are now available for CPython 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4070&#34;&gt;#4070&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Enable 3.12 CI (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4035&#34;&gt;#4035&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images in parallel (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4054&#34;&gt;#4054&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images with 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4055&#34;&gt;#4055&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/d9ad09a32b0e0481bb4fef548d35b7a49cc03c5d&#34;&gt;&lt;code&gt;d9ad09a&lt;/code&gt;&lt;/a&gt;
Prepare release 23.12.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4105&#34;&gt;#4105&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ebd543c0ac9b8a5f17636d0a42c425e5f693860e&#34;&gt;&lt;code&gt;ebd543c&lt;/code&gt;&lt;/a&gt;
Fix feature detection for parenthesized context managers (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4104&#34;&gt;#4104&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/eb7661f8ab9bff344835693c7c08789bb195137e&#34;&gt;&lt;code&gt;eb7661f&lt;/code&gt;&lt;/a&gt;
Fix another case where we format dummy implementation for
non-functions/class...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/0c9899956d890a9dc9c3adbc80b478a47846ced9&#34;&gt;&lt;code&gt;0c98999&lt;/code&gt;&lt;/a&gt;
Fix path in test message (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4102&#34;&gt;#4102&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/9aea9768cb60d23f2f4d331e94c4ee07ef1683a5&#34;&gt;&lt;code&gt;9aea976&lt;/code&gt;&lt;/a&gt;
Only use dummy implementation logic for functions and classes (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4066&#34;&gt;#4066&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/67b23d71854c19921cc6092c695d3301ab99229c&#34;&gt;&lt;code&gt;67b23d7&lt;/code&gt;&lt;/a&gt;
Bump actions/setup-python from 4 to 5 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4101&#34;&gt;#4101&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ce28be2705ab29f184ec4a00aa3d23340630796d&#34;&gt;&lt;code&gt;ce28be2&lt;/code&gt;&lt;/a&gt;
Add dedicated preview feature for East Asian Width (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4097&#34;&gt;#4097&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/61b529b7d15400309379f36104885a1dfcd2d026&#34;&gt;&lt;code&gt;61b529b&lt;/code&gt;&lt;/a&gt;
Allow empty lines at beginning of blocks (again) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4060&#34;&gt;#4060&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/e7e122e9ff27fc040a6e8ecd92f0e7603c87f92d&#34;&gt;&lt;code&gt;e7e122e&lt;/code&gt;&lt;/a&gt;
docs: Move &lt;code&gt;fmt: off&lt;/code&gt; docs (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4090&#34;&gt;#4090&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/432d9050c3d1e35a36ffc97d4a9e0e0c9e5e4ecc&#34;&gt;&lt;code&gt;432d905&lt;/code&gt;&lt;/a&gt;
docs: Unify option descriptions between &lt;code&gt;--help&lt;/code&gt; and
&lt;code&gt;the_basics.md&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4076&#34;&gt;#4076&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/23.11.0...23.12.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.11.0&amp;new-version=23.12.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`7d12fa0`](https://github.com/conijnio/pull-request-codecommit/commit/7d12fa0d53f337341682dd11bd88f0c2b46c1dac))

* chore(deps-dev): bump cryptography from 41.0.4 to 41.0.6 (#175)

Bumps [cryptography](https://github.com/pyca/cryptography) from 41.0.4
to 41.0.6.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst&#34;&gt;cryptography&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;41.0.6 - 2023-11-27&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;
* Fixed a null-pointer-dereference and segfault that could occur when
loading
certificates from a PKCS#7 bundle. Credit to **pkuzco** for reporting
the
  issue. **CVE-2023-49083**
&lt;p&gt;.. _v41-0-5:&lt;/p&gt;
&lt;p&gt;41.0.5 - 2023-10-24
&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Updated Windows, macOS, and Linux wheels to be compiled with OpenSSL
3.1.4.&lt;/li&gt;
&lt;li&gt;Added a function to support an upcoming &lt;code&gt;pyOpenSSL&lt;/code&gt;
release.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;.. _v41-0-4:&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/f09c261ca10a31fe41b1262306db7f8f1da0e48a&#34;&gt;&lt;code&gt;f09c261&lt;/code&gt;&lt;/a&gt;
41.0.6 release (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/9927&#34;&gt;#9927&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/5012bedaef2dc60af3955306774b77ef379116e3&#34;&gt;&lt;code&gt;5012bed&lt;/code&gt;&lt;/a&gt;
bump for 41.0.5 release (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/9766&#34;&gt;#9766&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/563b1193997512836603777d31e2ea281b3dc79a&#34;&gt;&lt;code&gt;563b119&lt;/code&gt;&lt;/a&gt;
Added binding needed for pyOpenSSL (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/9739&#34;&gt;#9739&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/9740&#34;&gt;#9740&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/pyca/cryptography/compare/41.0.4...41.0.6&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cryptography&amp;package-manager=pip&amp;previous-version=41.0.4&amp;new-version=41.0.6)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/pull-request-codecommit/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`ccfe5fd`](https://github.com/conijnio/pull-request-codecommit/commit/ccfe5fde2763bdc034dea540d5f3256e69c0d87c))

* chore(deps-dev): bump mypy from 1.7.0 to 1.7.1 (#174)

Bumps [mypy](https://github.com/python/mypy) from 1.7.0 to 1.7.1.
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/6b3c41838d8e7a39242b6fd035535e2d76eabfc6&#34;&gt;&lt;code&gt;6b3c418&lt;/code&gt;&lt;/a&gt;
Update version to 1.7.1 (without +dev)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c10e17348f2eacbbeae80eb6c10c661c0137d849&#34;&gt;&lt;code&gt;c10e173&lt;/code&gt;&lt;/a&gt;
[mypyc] Fix regression with nested functions (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16484&#34;&gt;#16484&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/e6399d10b0a1cdb104559482fad1b4dc0e2de6ac&#34;&gt;&lt;code&gt;e6399d1&lt;/code&gt;&lt;/a&gt;
Fix polymorphic application for callback protocols (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16514&#34;&gt;#16514&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/661adb756800ecc40fabbe62e9339efd253aff4e&#34;&gt;&lt;code&gt;661adb7&lt;/code&gt;&lt;/a&gt;
Fix crash on strict-equality with recursive types (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16483&#34;&gt;#16483&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/6c8e0cc47c014894ea41621a10f3d1b465322362&#34;&gt;&lt;code&gt;6c8e0cc&lt;/code&gt;&lt;/a&gt;
Ignore position if imprecise arguments are matched by name (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16471&#34;&gt;#16471&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/5c354c41c0fbb74418afcbd30ba822694be28d11&#34;&gt;&lt;code&gt;5c354c4&lt;/code&gt;&lt;/a&gt;
Fix missing meet case exposed by len narrowing (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16470&#34;&gt;#16470&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/88791cabe0521f77b699405154d90f3bb7c6b31b&#34;&gt;&lt;code&gt;88791ca&lt;/code&gt;&lt;/a&gt;
Exclude private attributes from override checks (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16464&#34;&gt;#16464&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/4b5b316beb570bba4c9b7797deb2e6d7df0552d0&#34;&gt;&lt;code&gt;4b5b316&lt;/code&gt;&lt;/a&gt;
Special-case unions in polymorphic inference (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16461&#34;&gt;#16461&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f862d3ef540c38e7efd2fffd64fc732d6318dfb4&#34;&gt;&lt;code&gt;f862d3e&lt;/code&gt;&lt;/a&gt;
Fix crash on Callable self in &lt;strong&gt;call&lt;/strong&gt; (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16453&#34;&gt;#16453&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/fe79a59e44299a3cc8025aa5084e08773c872a54&#34;&gt;&lt;code&gt;fe79a59&lt;/code&gt;&lt;/a&gt;
Bump version to 1.7.1+dev&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.7.0...v1.7.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.7.0&amp;new-version=1.7.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`3a12e8d`](https://github.com/conijnio/pull-request-codecommit/commit/3a12e8d2f75280009db0204a595b8b7bbbfaea4b))

* chore(deps-dev): bump mypy from 1.6.1 to 1.7.0 (#173)

Bumps [mypy](https://github.com/python/mypy) from 1.6.1 to 1.7.0.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python/mypy/blob/master/CHANGELOG.md&#34;&gt;mypy&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;Mypy Release Notes&lt;/h1&gt;
&lt;h2&gt;Next release&lt;/h2&gt;
&lt;p&gt;Stubgen will now include &lt;code&gt;__all__&lt;/code&gt; in its output if it is
in the input file (PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16356&#34;&gt;16356&lt;/a&gt;).&lt;/p&gt;
&lt;h2&gt;Mypy 1.7&lt;/h2&gt;
&lt;p&gt;We’ve just uploaded mypy 1.7 to the Python Package Index (&lt;a
href=&#34;https://pypi.org/project/mypy/&#34;&gt;PyPI&lt;/a&gt;). Mypy is a static type
checker for Python. This release includes new features, performance
improvements and bug fixes. You can install it as follows:&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;python3 -m pip install -U mypy
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;You can read the full documentation for this release on &lt;a
href=&#34;http://mypy.readthedocs.io&#34;&gt;Read the Docs&lt;/a&gt;.&lt;/p&gt;
&lt;h4&gt;Using TypedDict for &lt;code&gt;**kwargs&lt;/code&gt; Typing&lt;/h4&gt;
&lt;p&gt;Mypy now has support for using &lt;code&gt;Unpack[...]&lt;/code&gt; with a
TypedDict type to annotate &lt;code&gt;**kwargs&lt;/code&gt; arguments enabled by
default. Example:&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;# Or &#39;from typing_extensions import ...&#39;
from typing import TypedDict, Unpack
&lt;p&gt;class Person(TypedDict):
name: str
age: int&lt;/p&gt;
&lt;p&gt;def foo(**kwargs: Unpack[Person]) -&amp;gt; None:
...&lt;/p&gt;
&lt;p&gt;foo(name=&amp;quot;x&amp;quot;, age=1)  # Ok
foo(name=1)  # Error
&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;
&lt;p&gt;The definition of &lt;code&gt;foo&lt;/code&gt; above is equivalent to the one
below, with keyword-only arguments &lt;code&gt;name&lt;/code&gt; and
&lt;code&gt;age&lt;/code&gt;:&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;def foo(*, name: str, age: int) -&amp;gt; None:
    ...
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;Refer to &lt;a href=&#34;https://peps.python.org/pep-0692/&#34;&gt;PEP 692&lt;/a&gt; for
more information. Note that unlike in the current version of the PEP,
mypy always treats signatures with &lt;code&gt;Unpack[SomeTypedDict]&lt;/code&gt; as
equivalent to their expanded forms with explicit keyword arguments, and
there aren&#39;t special type checking rules for TypedDict arguments.&lt;/p&gt;
&lt;p&gt;This was contributed by Ivan Levkivskyi back in 2022 (PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/13471&#34;&gt;13471&lt;/a&gt;).&lt;/p&gt;
&lt;h4&gt;TypeVarTuple Support Enabled (Experimental)&lt;/h4&gt;
&lt;p&gt;Mypy now has support for variadic generics (TypeVarTuple) enabled by
default, as an experimental feature. Refer to &lt;a
href=&#34;https://peps.python.org/pep-0646/&#34;&gt;PEP 646&lt;/a&gt; for the
details.&lt;/p&gt;
&lt;p&gt;TypeVarTuple was implemented by Jared Hance and Ivan Levkivskyi over
several mypy releases, with help from Jukka Lehtosalo.&lt;/p&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f6b9972329d5d68f6defc92a10cc4c3bc339c27b&#34;&gt;&lt;code&gt;f6b9972&lt;/code&gt;&lt;/a&gt;
Remove +dev from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/62bcae2d9bad12c5d3b5dda23dc031e1c7ddf136&#34;&gt;&lt;code&gt;62bcae2&lt;/code&gt;&lt;/a&gt;
Fix handling of tuple type context with unpacks (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16444&#34;&gt;#16444&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c22294a80b000ea673e407994ac5111644944486&#34;&gt;&lt;code&gt;c22294a&lt;/code&gt;&lt;/a&gt;
Handle TypeVarTupleType when checking overload constraints (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16428&#34;&gt;#16428&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/8813968abb657113df5edfa207db46b0649c9dce&#34;&gt;&lt;code&gt;8813968&lt;/code&gt;&lt;/a&gt;
Fix type narrowing in lambda expressions (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16407&#34;&gt;#16407&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/681e54cfe1642adddc41c4ff11198b8bc955d5af&#34;&gt;&lt;code&gt;681e54c&lt;/code&gt;&lt;/a&gt;
Fix crash on unpack call special-casing (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16381&#34;&gt;#16381&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f68f46351e30644aefd19900ba1634595adc1d09&#34;&gt;&lt;code&gt;f68f463&lt;/code&gt;&lt;/a&gt;
Fix file reloading in dmypy with --export-types (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16359&#34;&gt;#16359&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/5624f401b3786ebdbe167c27297ed778cce3faa5&#34;&gt;&lt;code&gt;5624f40&lt;/code&gt;&lt;/a&gt;
Fix daemon crash caused by deleted submodule (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16370&#34;&gt;#16370&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/ad0e183b0df7cc3dd94d9e1cd6f5710859beda96&#34;&gt;&lt;code&gt;ad0e183&lt;/code&gt;&lt;/a&gt;
Enable Unpack/TypeVarTuple support (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16354&#34;&gt;#16354&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/b064a5c183b53a84d895bb8e3c36a3a74e24be9c&#34;&gt;&lt;code&gt;b064a5c&lt;/code&gt;&lt;/a&gt;
Fix dmypy inspect on Windows (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16355&#34;&gt;#16355&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/4e30e896486b774cdecaef6d3521a585b8acf8bc&#34;&gt;&lt;code&gt;4e30e89&lt;/code&gt;&lt;/a&gt;
Fix dmypy inspect for namespace packages (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16357&#34;&gt;#16357&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.6.1...v1.7.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.6.1&amp;new-version=1.7.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`826a694`](https://github.com/conijnio/pull-request-codecommit/commit/826a694808a015f5a5e73444c097e48694a1f6e0))

* chore(deps-dev): bump black from 23.10.1 to 23.11.0 (#172)

Bumps [black](https://github.com/psf/black) from 23.10.1 to 23.11.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.11.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Support formatting ranges of lines with the new
&lt;code&gt;--line-ranges&lt;/code&gt; command-line option
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4020&#34;&gt;#4020&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix crash on formatting bytes strings that look like docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4003&#34;&gt;#4003&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash when whitespace followed a backslash before newline in a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4008&#34;&gt;#4008&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix standalone comments inside complex blocks crashing Black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4016&#34;&gt;#4016&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on formatting code like &lt;code&gt;await (a ** b)&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3994&#34;&gt;#3994&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;No longer treat leading f-strings as docstrings. This matches
Python&#39;s behaviour and
fixes a crash (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4019&#34;&gt;#4019&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Multiline dicts and lists that are the sole argument to a function
are now
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3964&#34;&gt;#3964&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Multiline unpacked dicts and lists as the sole argument to a
function are now also
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3992&#34;&gt;#3992&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;In f-string debug expressions, quote types that are visible in the
final string
are now preserved (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4005&#34;&gt;#4005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug where long &lt;code&gt;case&lt;/code&gt; blocks were not split into
multiple lines. Also enable
general trailing comma rules on &lt;code&gt;case&lt;/code&gt; blocks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep requiring two empty lines between module-level docstring and
first function or
class definition (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4028&#34;&gt;#4028&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for single-line format skip with other comments on the
same line (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3959&#34;&gt;#3959&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Consistently apply force exclusion logic before resolving symlinks
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4015&#34;&gt;#4015&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug in the matching of absolute path names in
&lt;code&gt;--include&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3976&#34;&gt;#3976&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Performance&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix mypyc builds on arm64 on macOS (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4017&#34;&gt;#4017&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black&#39;s pre-commit integration will now run only on git hooks
appropriate for a code
formatter (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3940&#34;&gt;#3940&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.11.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Support formatting ranges of lines with the new
&lt;code&gt;--line-ranges&lt;/code&gt; command-line option
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4020&#34;&gt;#4020&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix crash on formatting bytes strings that look like docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4003&#34;&gt;#4003&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash when whitespace followed a backslash before newline in a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4008&#34;&gt;#4008&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix standalone comments inside complex blocks crashing Black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4016&#34;&gt;#4016&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on formatting code like &lt;code&gt;await (a ** b)&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3994&#34;&gt;#3994&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;No longer treat leading f-strings as docstrings. This matches
Python&#39;s behaviour and
fixes a crash (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4019&#34;&gt;#4019&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Multiline dicts and lists that are the sole argument to a function
are now indented
less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3964&#34;&gt;#3964&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Multiline unpacked dicts and lists as the sole argument to a
function are now also
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3992&#34;&gt;#3992&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;In f-string debug expressions, quote types that are visible in the
final string are
now preserved (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4005&#34;&gt;#4005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug where long &lt;code&gt;case&lt;/code&gt; blocks were not split into
multiple lines. Also enable
general trailing comma rules on &lt;code&gt;case&lt;/code&gt; blocks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep requiring two empty lines between module-level docstring and
first function or
class definition (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4028&#34;&gt;#4028&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for single-line format skip with other comments on the
same line (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3959&#34;&gt;#3959&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Consistently apply force exclusion logic before resolving symlinks
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4015&#34;&gt;#4015&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug in the matching of absolute path names in
&lt;code&gt;--include&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3976&#34;&gt;#3976&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Performance&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix mypyc builds on arm64 on macOS (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4017&#34;&gt;#4017&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black&#39;s pre-commit integration will now run only on git hooks
appropriate for a code
formatter (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3940&#34;&gt;#3940&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/2a1c67e0b2f81df602ec1f6e7aeb030b9709dc7c&#34;&gt;&lt;code&gt;2a1c67e&lt;/code&gt;&lt;/a&gt;
Prepare release 23.11.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4032&#34;&gt;#4032&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/72e7a2e43eef2aa0c83652bb6725eb004a2a69f3&#34;&gt;&lt;code&gt;72e7a2e&lt;/code&gt;&lt;/a&gt;
Remove redundant condition from &lt;code&gt;has_magic_trailing_comma&lt;/code&gt;
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4023&#34;&gt;#4023&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/1a7d9c2f58de1ffcbbe6d133f60f283601ba3f54&#34;&gt;&lt;code&gt;1a7d9c2&lt;/code&gt;&lt;/a&gt;
Preserve visible quote types for f-string debug expressions (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4005&#34;&gt;#4005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/f4c7be5445c87d9af5eba3d12faea62d2635e3d8&#34;&gt;&lt;code&gt;f4c7be5&lt;/code&gt;&lt;/a&gt;
docs: fix minor typo (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4030&#34;&gt;#4030&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/2e4fac9d87615e904a49e46a9cab2293e0b13126&#34;&gt;&lt;code&gt;2e4fac9&lt;/code&gt;&lt;/a&gt;
Apply force exclude logic before symlink resolution (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4015&#34;&gt;#4015&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/66008fda5dc07f5626e5f5d0dcefc476a9c12ab8&#34;&gt;&lt;code&gt;66008fd&lt;/code&gt;&lt;/a&gt;
[563] Fix standalone comments inside complex blocks crashing Black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4016&#34;&gt;#4016&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/50ed6221d97b265025abaa66116a7b185f2df5e2&#34;&gt;&lt;code&gt;50ed622&lt;/code&gt;&lt;/a&gt;
Fix long case blocks not split into multiple lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/46be1f8e54ac9a7d67723c0fa28c7bec13a0a2bf&#34;&gt;&lt;code&gt;46be1f8&lt;/code&gt;&lt;/a&gt;
Support formatting specified lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4020&#34;&gt;#4020&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ecbd9e8cf71f13068c7e6803a534e00363114c91&#34;&gt;&lt;code&gt;ecbd9e8&lt;/code&gt;&lt;/a&gt;
Fix crash with f-string docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4019&#34;&gt;#4019&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/e808e61db8c7a8f9c7fd4b2fff2281141f6b2517&#34;&gt;&lt;code&gt;e808e61&lt;/code&gt;&lt;/a&gt;
Preview: Keep requiring two empty lines between module-level docstring
and fi...&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/23.10.1...23.11.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.10.1&amp;new-version=23.11.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`8b1c3da`](https://github.com/conijnio/pull-request-codecommit/commit/8b1c3daa7784d3e9e6884fc879e7f32cf3e546c2))

* chore(deps-dev): bump pytest from 7.4.2 to 7.4.3 (#171)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.2 to
7.4.3.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;pytest 7.4.3 (2023-10-24)&lt;/h2&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/10447&#34;&gt;#10447&lt;/a&gt;:
Markers are now considered in the reverse mro order to ensure base class
markers are considered first -- this resolves a regression.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11239&#34;&gt;#11239&lt;/a&gt;:
Fixed &lt;code&gt;:=&lt;/code&gt; in asserts impacting unrelated test cases.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11439&#34;&gt;#11439&lt;/a&gt;:
Handled an edge case where :data:&lt;code&gt;sys.stderr&lt;/code&gt; might already
be closed when :ref:&lt;code&gt;faulthandler&lt;/code&gt; is tearing down.&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/23906106968eb95afbd61adfbc7bbb795fc9aaa9&#34;&gt;&lt;code&gt;2390610&lt;/code&gt;&lt;/a&gt;
Tweak changelog.rst&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a0714aa0076f38e6fb8c7321e8bb4f5f33d1792d&#34;&gt;&lt;code&gt;a0714aa&lt;/code&gt;&lt;/a&gt;
Prepare release version 7.4.3&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/44ad1c9811d2ebf540e601ea66b9bebf8ea82969&#34;&gt;&lt;code&gt;44ad1c9&lt;/code&gt;&lt;/a&gt;
[7.4.x] fix &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/10447&#34;&gt;#10447&lt;/a&gt;
- consider marks in reverse mro order to give base classes...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/5dc77253d439038ac64c55a5a48692ac3a53db2e&#34;&gt;&lt;code&gt;5dc7725&lt;/code&gt;&lt;/a&gt;
[7.4.x] Ensure logging tests always cleanup after themselves (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11541&#34;&gt;#11541&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a5178273183ddbda0ef4e4c6aa2b92aab086776b&#34;&gt;&lt;code&gt;a517827&lt;/code&gt;&lt;/a&gt;
[7.4.x] Configure ReadTheDocs to fail on warnings (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11540&#34;&gt;#11540&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/21fe071d797612468fa18dd0ae4d6dbf49846b6d&#34;&gt;&lt;code&gt;21fe071&lt;/code&gt;&lt;/a&gt;
[7.4.x] fix for ValueError raised in faulthandler teardown code (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11455&#34;&gt;#11455&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/f8bb8572fed8627946bfc82819d24b138d587257&#34;&gt;&lt;code&gt;f8bb857&lt;/code&gt;&lt;/a&gt;
Force terminal width when running tests (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11425&#34;&gt;#11425&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11432&#34;&gt;#11432&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/1944dc06d39404ae9869b544dc2e2b482bf472e2&#34;&gt;&lt;code&gt;1944dc0&lt;/code&gt;&lt;/a&gt;
[7.4.x] Fix --import-mode=importlib when root contains
&lt;code&gt;__init__.py&lt;/code&gt; file (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/1&#34;&gt;#1&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/946634c84cf074a1ead10bdba56ddf3e5408e95c&#34;&gt;&lt;code&gt;946634c&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11419&#34;&gt;#11419&lt;/a&gt;
from nicoddemus/backport-11414-to-7.4.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d849a3ed64c6da63a0e3713892a7bfefdd56acaf&#34;&gt;&lt;code&gt;d849a3e&lt;/code&gt;&lt;/a&gt;
[7.4.x] fix: closes &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11343&#34;&gt;#11343&lt;/a&gt;&#39;s
[attr-defined] type errors (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11421&#34;&gt;#11421&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/7.4.2...7.4.3&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=7.4.2&amp;new-version=7.4.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`a47fa59`](https://github.com/conijnio/pull-request-codecommit/commit/a47fa5939c35bdcd0b81f6f9a8b811b9cedaec11))

* chore(deps-dev): bump black from 23.10.0 to 23.10.1 (#170)

Bumps [black](https://github.com/psf/black) from 23.10.0 to 23.10.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.1&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Maintanence release to get a fix out for GitHub Action edge case (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix merging implicit multiline strings that have inline comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3956&#34;&gt;#3956&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty first line after block open before a comment or compound
statement (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Change Dockerfile to hatch + compile black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3965&#34;&gt;#3965&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The summary output for GitHub workflows is now suppressible using
the &lt;code&gt;summary&lt;/code&gt;
parameter. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3958&#34;&gt;#3958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix the action failing when Black check doesn&#39;t pass (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;It is known Windows documentation CI is broken
&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3968&#34;&gt;psf/black#3968&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.1&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Maintanence release to get a fix out for GitHub Action edge case (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix merging implicit multiline strings that have inline comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3956&#34;&gt;#3956&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty first line after block open before a comment or compound
statement (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Change Dockerfile to hatch + compile black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3965&#34;&gt;#3965&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The summary output for GitHub workflows is now suppressible using
the &lt;code&gt;summary&lt;/code&gt;
parameter. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3958&#34;&gt;#3958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix the action failing when Black check doesn&#39;t pass (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;It is known Windows documentation CI is broken
&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3968&#34;&gt;psf/black#3968&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/744d23b34800c06e10272149b70752396e90eeb8&#34;&gt;&lt;code&gt;744d23b&lt;/code&gt;&lt;/a&gt;
Prepare release 23.10.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3969&#34;&gt;#3969&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/8de4be516879302afce542ac80a6a43ced807759&#34;&gt;&lt;code&gt;8de4be5&lt;/code&gt;&lt;/a&gt;
Fix CI failing (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/c0adca321dc0d97a704de8ed0353e5b894a6a912&#34;&gt;&lt;code&gt;c0adca3&lt;/code&gt;&lt;/a&gt;
docs: specifies the use of the .git-blame-ignore-revs file (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3961&#34;&gt;#3961&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/a7643fac8d97c15640a2b1a79f68b3dc771aebfb&#34;&gt;&lt;code&gt;a7643fa&lt;/code&gt;&lt;/a&gt;
Add summary parameter to action (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3958&#34;&gt;#3958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/d291c2338c3c1feee4f3f26985c0964ec1b7eb9f&#34;&gt;&lt;code&gt;d291c23&lt;/code&gt;&lt;/a&gt;
Move Docker image to hatch + compile (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3965&#34;&gt;#3965&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/7f1c578b89b2c256a6ce3b70fc1b970b3ffa3349&#34;&gt;&lt;code&gt;7f1c578&lt;/code&gt;&lt;/a&gt;
Bump peter-evans/create-or-update-comment from 3.0.2 to 3.1.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3966&#34;&gt;#3966&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/2db5ab0a7b3b321e4cec70964239ee88087cd810&#34;&gt;&lt;code&gt;2db5ab0&lt;/code&gt;&lt;/a&gt;
Allow empty line after block open before a comment or compound statement
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/0a37888e79059018eef9293a724b14da59d3377a&#34;&gt;&lt;code&gt;0a37888&lt;/code&gt;&lt;/a&gt;
Fix typos in CHANGES.md (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3963&#34;&gt;#3963&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/882d8795c6ff65c02f2657e596391748d1b6b7f5&#34;&gt;&lt;code&gt;882d879&lt;/code&gt;&lt;/a&gt;
Fix merging implicit multiline strings that have inline comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3956&#34;&gt;#3956&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/psf/black/compare/23.10.0...23.10.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.10.0&amp;new-version=23.10.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`eec7824`](https://github.com/conijnio/pull-request-codecommit/commit/eec7824595dbf33e4e4d1cffb93fcd8f45cedcec))

* chore(deps-dev): bump black from 23.9.1 to 23.10.0 (#167)

Bumps [black](https://github.com/psf/black) from 23.9.1 to 23.10.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.0&lt;/h2&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix comments getting removed from inside parenthesized strings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3909&#34;&gt;#3909&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix long lines with power operators getting split before the line
length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3942&#34;&gt;#3942&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Long type hints are now wrapped in parentheses and properly indented
when split across
multiple lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3899&#34;&gt;#3899&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Magic trailing commas are now respected in return types. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3916&#34;&gt;#3916&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Require one empty line after module-level docstrings. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Treat raw triple-quoted strings as docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix cache versioning logic when &lt;code&gt;BLACK_CACHE_DIR&lt;/code&gt; is set
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3937&#34;&gt;#3937&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Parser&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where attributes named &lt;code&gt;type&lt;/code&gt; were not acccepted
inside &lt;code&gt;match&lt;/code&gt; statements
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3950&#34;&gt;#3950&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for PEP 695 type aliases containing lambdas and other
unusual expressions
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3949&#34;&gt;#3949&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Output&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black no longer attempts to provide special errors for attempting to
format Python 2
code (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3933&#34;&gt;#3933&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Black will more consistently print stacktraces on internal errors in
verbose mode
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3938&#34;&gt;#3938&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The action output displayed in the job summary is now wrapped in
Markdown (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3914&#34;&gt;#3914&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.0&lt;/h2&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix comments getting removed from inside parenthesized strings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3909&#34;&gt;#3909&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix long lines with power operators getting split before the line
length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3942&#34;&gt;#3942&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Long type hints are now wrapped in parentheses and properly indented
when split across
multiple lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3899&#34;&gt;#3899&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Magic trailing commas are now respected in return types. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3916&#34;&gt;#3916&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Require one empty line after module-level docstrings. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Treat raw triple-quoted strings as docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix cache versioning logic when &lt;code&gt;BLACK_CACHE_DIR&lt;/code&gt; is set
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3937&#34;&gt;#3937&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Parser&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where attributes named &lt;code&gt;type&lt;/code&gt; were not acccepted
inside &lt;code&gt;match&lt;/code&gt; statements
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3950&#34;&gt;#3950&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for PEP 695 type aliases containing lambdas and other
unusual expressions
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3949&#34;&gt;#3949&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Output&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black no longer attempts to provide special errors for attempting to
format Python 2
code (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3933&#34;&gt;#3933&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Black will more consistently print stacktraces on internal errors in
verbose mode
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3938&#34;&gt;#3938&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The action output displayed in the job summary is now wrapped in
Markdown (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3914&#34;&gt;#3914&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/9edba85f71d50d12996ef7bda576426362016171&#34;&gt;&lt;code&gt;9edba85&lt;/code&gt;&lt;/a&gt;
Prepare release 23.10.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3951&#34;&gt;#3951&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/bb588073ab286a9f1f8d839ab2cebe13011dd22c&#34;&gt;&lt;code&gt;bb58807&lt;/code&gt;&lt;/a&gt;
Fix parser bug where &amp;quot;type&amp;quot; was misinterpreted as a keyword
inside a match (#...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/722735d20ebdc66c0da0e0df7658293455694500&#34;&gt;&lt;code&gt;722735d&lt;/code&gt;&lt;/a&gt;
Fix grammar for type alias support (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3949&#34;&gt;#3949&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/abe57e3d92727f1b26c717fad3978159b987fe79&#34;&gt;&lt;code&gt;abe57e3&lt;/code&gt;&lt;/a&gt;
Treat raw strings like other docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/1648ac51806d092c95cb9bb2e4a5bffda6095bc1&#34;&gt;&lt;code&gt;1648ac5&lt;/code&gt;&lt;/a&gt;
Fix long lines with power operator(s) getting splitted before line
length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3&#34;&gt;#3&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/6f84f652850dca8a1b578581e2fbb2cb95e791cc&#34;&gt;&lt;code&gt;6f84f65&lt;/code&gt;&lt;/a&gt;
Migrate mypy config to pyproject.toml (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3936&#34;&gt;#3936&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/3bb92146f59804a6ead47d5f2d0fdc47daa6b698&#34;&gt;&lt;code&gt;3bb9214&lt;/code&gt;&lt;/a&gt;
CI Test: Deprecating &#39;Healthcheck.all()&#39; from Hypothesis in fuzz.py (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3945&#34;&gt;#3945&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/935f303a0a7b794e722c7df00c906be285884874&#34;&gt;&lt;code&gt;935f303&lt;/code&gt;&lt;/a&gt;
Fix test that was not being run (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3939&#34;&gt;#3939&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/b7717c3f1e73d6b847e2534a2cebbb657b96caf8&#34;&gt;&lt;code&gt;b7717c3&lt;/code&gt;&lt;/a&gt;
Standardise newlines after module-level docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/7aa37ea0adf864baf3ef3dfbcfaf5ff1ff780250&#34;&gt;&lt;code&gt;7aa37ea&lt;/code&gt;&lt;/a&gt;
Report all stacktraces in verbose mode (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3938&#34;&gt;#3938&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/23.9.1...23.10.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.9.1&amp;new-version=23.10.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`b0dde0b`](https://github.com/conijnio/pull-request-codecommit/commit/b0dde0b4eb1571728d290e62ae32a20386ddb86e))

* chore(deps-dev): bump pygments from 2.14.0 to 2.15.0 (#157)

Bumps [pygments](https://github.com/pygments/pygments) from 2.14.0 to
2.15.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pygments/pygments/releases&#34;&gt;pygments&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;2.15.0&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;Added lexers:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Carbon (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2362&#34;&gt;#2362&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2365&#34;&gt;#2365&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2366&#34;&gt;#2366&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2367&#34;&gt;#2367&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2368&#34;&gt;#2368&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2369&#34;&gt;#2369&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2370&#34;&gt;#2370&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Dax (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2335&#34;&gt;#2335&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2345&#34;&gt;#2345&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;MediaWiki Wikitext (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2373&#34;&gt;#2373&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/827&#34;&gt;#827&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;PostgreSQL Explain (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2398&#34;&gt;#2398&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;WGSL (WebGPU Shading Language) (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2386&#34;&gt;#2386&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;X++ (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2339&#34;&gt;#2339&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Updated lexers:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;AMDGPU: Add support for &lt;code&gt;scratch_&lt;/code&gt; instructions, the
&lt;code&gt;attr*.*&lt;/code&gt; argument,
as well as the &lt;code&gt;off&lt;/code&gt; modifier (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2327&#34;&gt;#2327&lt;/a&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;APDL: Miscellaneous improvements (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2314&#34;&gt;#2314&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;bash/tcsh:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Move &lt;code&gt;break&lt;/code&gt; to keywords (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2377&#34;&gt;#2377&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Improve bash math expansion lexing (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2255&#34;&gt;#2255&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2353&#34;&gt;#2353&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Chapel: Support attributes (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2376&#34;&gt;#2376&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;CMake: Implement bracket style comments (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2338&#34;&gt;#2338&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2354&#34;&gt;#2354&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;CSS: Improve lexing of numbers inside function calls (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2382&#34;&gt;#2382&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2383&#34;&gt;#2383&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;diff: Support normal diff syntax, as opposed to unified diff syntax
(&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2321&#34;&gt;#2321&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;GLSL, HLSL:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Support line continuations in preprocessor code (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2350&#34;&gt;#2350&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Improve preprocessor directive handling (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2357&#34;&gt;#2357&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;LilyPond: minor update of builtins&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;PHP: support attributes (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2055&#34;&gt;#2055&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2347&#34;&gt;#2347&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2360&#34;&gt;#2360&lt;/a&gt;),
fix anonymous classes without
parameters (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2359&#34;&gt;#2359&lt;/a&gt;),
improve lexing of variable variable syntax (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2358&#34;&gt;#2358&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Python:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Add missing builtins (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2334&#34;&gt;#2334&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix inconsistent lexing of &lt;code&gt;None&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2406&#34;&gt;#2406&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Rebol/Red: Don&#39;t require script headers (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2348&#34;&gt;#2348&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2349&#34;&gt;#2349&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Spice: Update keywords (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2336&#34;&gt;#2336&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;SQL+Jinja (&lt;code&gt;analyse_text&lt;/code&gt; method): Fix catastrophic
backtracking (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2355&#34;&gt;#2355&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Terraform: Add &lt;code&gt;hcl&lt;/code&gt; alias (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2375&#34;&gt;#2375&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Declare support for Python 3.11 and drop support for Python 3.6 (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2324&#34;&gt;#2324&lt;/a&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Update &lt;code&gt;native&lt;/code&gt; style to improve contrast (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2325&#34;&gt;#2325&lt;/a&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Update `github-dark`` style to match latest Primer style (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2401&#34;&gt;#2401&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Revert a change that made guessing lexers based on file names slower
on Python 3.10 and older (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2328&#34;&gt;#2328&lt;/a&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Fix some places where a locale-dependent encoding could
unintentionally
be used instead of UTF-8 (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2326&#34;&gt;#2326&lt;/a&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Fix Python traceback handling (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2226&#34;&gt;#2226&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2329&#34;&gt;#2329&lt;/a&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pygments/pygments/blob/master/CHANGES&#34;&gt;pygments&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;Version 2.15.0&lt;/h2&gt;
&lt;p&gt;(released April 10th, 2023)&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;Added lexers:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Carbon (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2362&#34;&gt;#2362&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2365&#34;&gt;#2365&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2366&#34;&gt;#2366&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2367&#34;&gt;#2367&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2368&#34;&gt;#2368&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2369&#34;&gt;#2369&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2370&#34;&gt;#2370&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Dax (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2335&#34;&gt;#2335&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2345&#34;&gt;#2345&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;MediaWiki Wikitext (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2373&#34;&gt;#2373&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/827&#34;&gt;#827&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;PostgreSQL Explain (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2398&#34;&gt;#2398&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;WGSL (WebGPU Shading Language) (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2386&#34;&gt;#2386&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;X++ (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2339&#34;&gt;#2339&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Updated lexers:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;AMDGPU: Add support for &lt;code&gt;scratch_&lt;/code&gt; instructions, the
&lt;code&gt;attr*.*&lt;/code&gt; argument,
as well as the &lt;code&gt;off&lt;/code&gt; modifier (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2327&#34;&gt;#2327&lt;/a&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;APDL: Miscellaneous improvements (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2314&#34;&gt;#2314&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;bash/tcsh:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Move &lt;code&gt;break&lt;/code&gt; to keywords (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2377&#34;&gt;#2377&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Improve bash math expansion lexing (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2255&#34;&gt;#2255&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2353&#34;&gt;#2353&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Chapel: Support attributes (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2376&#34;&gt;#2376&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;CMake: Implement bracket style comments (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2338&#34;&gt;#2338&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2354&#34;&gt;#2354&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;CSS: Improve lexing of numbers inside function calls (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2382&#34;&gt;#2382&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2383&#34;&gt;#2383&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;diff: Support normal diff syntax, as opposed to unified diff syntax
(&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2321&#34;&gt;#2321&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;GLSL, HLSL:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Support line continuations in preprocessor code (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2350&#34;&gt;#2350&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Improve preprocessor directive handling (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2357&#34;&gt;#2357&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;LilyPond: minor update of builtins&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;PHP: support attributes (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2055&#34;&gt;#2055&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2347&#34;&gt;#2347&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2360&#34;&gt;#2360&lt;/a&gt;),
fix anonymous classes without
parameters (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2359&#34;&gt;#2359&lt;/a&gt;),
improve lexing of variable variable syntax (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2358&#34;&gt;#2358&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Python:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Add missing builtins (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2334&#34;&gt;#2334&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix inconsistent lexing of &lt;code&gt;None&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2406&#34;&gt;#2406&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Rebol/Red: Don&#39;t require script headers (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2348&#34;&gt;#2348&lt;/a&gt;,
&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2349&#34;&gt;#2349&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Spice: Update keywords (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2336&#34;&gt;#2336&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;SQL+Jinja (&lt;code&gt;analyse_text&lt;/code&gt; method): Fix catastrophic
backtracking (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2355&#34;&gt;#2355&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Terraform: Add &lt;code&gt;hcl&lt;/code&gt; alias (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2375&#34;&gt;#2375&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Declare support for Python 3.11 and drop support for Python 3.6 (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2324&#34;&gt;#2324&lt;/a&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Update &lt;code&gt;native&lt;/code&gt; style to improve contrast (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2325&#34;&gt;#2325&lt;/a&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Update `github-dark`` style to match latest Primer style (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2401&#34;&gt;#2401&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;Revert a change that made guessing lexers based on file names slower
on Python 3.10 and older (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2328&#34;&gt;#2328&lt;/a&gt;).&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pygments/pygments/commit/6c187ad83267be9ce142af3fd5c9e670339dc7aa&#34;&gt;&lt;code&gt;6c187ad&lt;/code&gt;&lt;/a&gt;
Prepare 2.15 release.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pygments/pygments/commit/00b9cb022cc9c05784c43c11bd7f73e64008b347&#34;&gt;&lt;code&gt;00b9cb0&lt;/code&gt;&lt;/a&gt;
Prepare for release.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pygments/pygments/commit/a0824a45f0bd6c45528fa16132f09dd3570a8234&#34;&gt;&lt;code&gt;a0824a4&lt;/code&gt;&lt;/a&gt;
Update CHANGES&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pygments/pygments/commit/26f9f6c852846fe579c37fe936a872b68fa686ba&#34;&gt;&lt;code&gt;26f9f6c&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2406&#34;&gt;#2406&lt;/a&gt;
from rdbende/fix-fromimport-none&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pygments/pygments/commit/62b1bbbe6e329268eaa4c68f0e3eb8867c450acc&#34;&gt;&lt;code&gt;62b1bbb&lt;/code&gt;&lt;/a&gt;
Change token of None after from keyword&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pygments/pygments/commit/acee60e4e8dde9ea99fc494740e20b06188791ac&#34;&gt;&lt;code&gt;acee60e&lt;/code&gt;&lt;/a&gt;
Update CHANGES&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pygments/pygments/commit/eaca69091119e0ac5c97e626ba9e3b21b688c5ed&#34;&gt;&lt;code&gt;eaca690&lt;/code&gt;&lt;/a&gt;
Add lexer for MediaWiki Wikitext (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2373&#34;&gt;#2373&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pygments/pygments/commit/0e9c87bcf096908956e031f15a4e589e83be1691&#34;&gt;&lt;code&gt;0e9c87b&lt;/code&gt;&lt;/a&gt;
Update CHANGES&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pygments/pygments/commit/ef0abbaece522732031d61391567c017d48d87b7&#34;&gt;&lt;code&gt;ef0abba&lt;/code&gt;&lt;/a&gt;
Add PostgreSQL Explain lexer (&lt;a
href=&#34;https://redirect.github.com/pygments/pygments/issues/2398&#34;&gt;#2398&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pygments/pygments/commit/3c6e2af8fbc44bb1ef77389d09118c37faea8746&#34;&gt;&lt;code&gt;3c6e2af&lt;/code&gt;&lt;/a&gt;
Update CHANGES&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pygments/pygments/compare/2.14.0...2.15.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pygments&amp;package-manager=pip&amp;previous-version=2.14.0&amp;new-version=2.15.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

You can trigger a rebase of this PR by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/pull-request-codecommit/network/alerts).

&lt;/details&gt;

&gt; **Note**
&gt; Automatic rebases have been disabled on this pull request as it has
been open for over 30 days.

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`8604315`](https://github.com/conijnio/pull-request-codecommit/commit/86043159555cb842feeb8c4d1c74b6a465c19bf9))

* chore(deps-dev): bump mypy from 1.6.0 to 1.6.1 (#169)

Bumps [mypy](https://github.com/python/mypy) from 1.6.0 to 1.6.1.
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/9b891fe5a101ecbb818f3f16641ab909f289ba04&#34;&gt;&lt;code&gt;9b891fe&lt;/code&gt;&lt;/a&gt;
Remove +dev from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/6b6504eb8a96fa6a9c7b8f034803eb9a0444fe86&#34;&gt;&lt;code&gt;6b6504e&lt;/code&gt;&lt;/a&gt;
Fix crash on ParamSpec unification (for real) (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16259&#34;&gt;#16259&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/eb81e63e9dec4dd4c75b307871d1ef9b3e350838&#34;&gt;&lt;code&gt;eb81e63&lt;/code&gt;&lt;/a&gt;
Fix crash on ParamSpec unification (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16251&#34;&gt;#16251&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/45f7a12e558e4a48446af3b36494dcb4045c1028&#34;&gt;&lt;code&gt;45f7a12&lt;/code&gt;&lt;/a&gt;
Add +dev to version&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.6.0...v1.6.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.6.0&amp;new-version=1.6.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`8e7e9de`](https://github.com/conijnio/pull-request-codecommit/commit/8e7e9de55ec95c687f02ae92dd84a29fb91497a3))

* chore: tweak dependabot (#168)

**Issue #, if available:**

## Description of changes:

Dependabot was not configured correctly

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [ ] Update tests
* [ ] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`969d0d0`](https://github.com/conijnio/pull-request-codecommit/commit/969d0d085c87535a8e97e6658306f762fc3ec3f7))

* chore: tweak dependabot

Dependabot was not configured correctly ([`932a95e`](https://github.com/conijnio/pull-request-codecommit/commit/932a95e48bf51789f35f9d13014519d8b4248ab6))

* chore(deps-dev): bump urllib3 from 1.26.17 to 1.26.18 (#166) ([`f438076`](https://github.com/conijnio/pull-request-codecommit/commit/f4380766627663848e4f488cb67265d497db377a))

* chore(deps-dev): bump urllib3 from 1.26.17 to 1.26.18

Bumps [urllib3](https://github.com/urllib3/urllib3) from 1.26.17 to 1.26.18.
- [Release notes](https://github.com/urllib3/urllib3/releases)
- [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
- [Commits](https://github.com/urllib3/urllib3/compare/1.26.17...1.26.18)

---
updated-dependencies:
- dependency-name: urllib3
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0fd3b7b`](https://github.com/conijnio/pull-request-codecommit/commit/0fd3b7b1cf3999704404bf63c9d88f2671711479))

* chore(deps-dev): bump mypy from 1.5.1 to 1.6.0 (#165) ([`4f802e2`](https://github.com/conijnio/pull-request-codecommit/commit/4f802e2f21d6c87acd3834c8a72f37f7cbda3435))

* chore(deps-dev): bump mypy from 1.5.1 to 1.6.0

Bumps [mypy](https://github.com/python/mypy) from 1.5.1 to 1.6.0.
- [Commits](https://github.com/python/mypy/compare/v1.5.1...v1.6.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0479553`](https://github.com/conijnio/pull-request-codecommit/commit/047955347d2c50f3d520603af9a97a8a1fcad790))

* chore(deps-dev): bump urllib3 from 1.26.14 to 1.26.17 (#164) ([`25437d0`](https://github.com/conijnio/pull-request-codecommit/commit/25437d098cddae513ef0cd3ddb2be864ea5bd61c))

* chore(deps-dev): bump urllib3 from 1.26.14 to 1.26.17

Bumps [urllib3](https://github.com/urllib3/urllib3) from 1.26.14 to 1.26.17.
- [Release notes](https://github.com/urllib3/urllib3/releases)
- [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
- [Commits](https://github.com/urllib3/urllib3/compare/1.26.14...1.26.17)

---
updated-dependencies:
- dependency-name: urllib3
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1fa120b`](https://github.com/conijnio/pull-request-codecommit/commit/1fa120be345d32f566d68282eb17ab173b34f4a8))

* chore(deps-dev): bump certifi from 2022.12.7 to 2023.7.22 (#163) ([`4c9e5cb`](https://github.com/conijnio/pull-request-codecommit/commit/4c9e5cb5ec46d7b094986eefa4f82c0695e95eea))

* chore(deps-dev): bump certifi from 2022.12.7 to 2023.7.22

Bumps [certifi](https://github.com/certifi/python-certifi) from 2022.12.7 to 2023.7.22.
- [Commits](https://github.com/certifi/python-certifi/compare/2022.12.07...2023.07.22)

---
updated-dependencies:
- dependency-name: certifi
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e4646b2`](https://github.com/conijnio/pull-request-codecommit/commit/e4646b2640c0d94ca90d0ea4eed13ca0b7dc1fd7))

* chore(deps-dev): bump cryptography from 41.0.3 to 41.0.4 (#162) ([`369dfc1`](https://github.com/conijnio/pull-request-codecommit/commit/369dfc1599031799838b37332ed20ae9234003bc))

* chore(deps-dev): bump cryptography from 41.0.3 to 41.0.4

Bumps [cryptography](https://github.com/pyca/cryptography) from 41.0.3 to 41.0.4.
- [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pyca/cryptography/compare/41.0.3...41.0.4)

---
updated-dependencies:
- dependency-name: cryptography
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`4f19615`](https://github.com/conijnio/pull-request-codecommit/commit/4f19615d5dbe1ca2b5e4c84dd6cb20a3670ac8f6))

* chore(deps-dev): bump black from 23.7.0 to 23.9.1 (#161) ([`53ed229`](https://github.com/conijnio/pull-request-codecommit/commit/53ed2298acc127d704e2c22c972ffa9122d20ea0))

* chore(deps-dev): bump black from 23.7.0 to 23.9.1

Bumps [black](https://github.com/psf/black) from 23.7.0 to 23.9.1.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.7.0...23.9.1)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`373fe7f`](https://github.com/conijnio/pull-request-codecommit/commit/373fe7f21d4446b845ff12e87c0538dd9098a866))

* chore(deps-dev): bump pytest from 7.4.1 to 7.4.2 (#160) ([`61667e9`](https://github.com/conijnio/pull-request-codecommit/commit/61667e9df23132cde642deeabf6caa7766e76e8b))

* chore(deps-dev): bump pytest from 7.4.1 to 7.4.2

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.1 to 7.4.2.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.4.1...7.4.2)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ed44d29`](https://github.com/conijnio/pull-request-codecommit/commit/ed44d2996c882e3a930b5bdb0db57a1cb91dd28c))

* chore(deps-dev): bump cryptography from 41.0.0 to 41.0.3 (#159) ([`48dc595`](https://github.com/conijnio/pull-request-codecommit/commit/48dc595689e9648980ac66bf936edddfee6cc0d0))

* chore(deps-dev): bump cryptography from 41.0.0 to 41.0.3

Bumps [cryptography](https://github.com/pyca/cryptography) from 41.0.0 to 41.0.3.
- [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pyca/cryptography/compare/41.0.0...41.0.3)

---
updated-dependencies:
- dependency-name: cryptography
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1a27e9d`](https://github.com/conijnio/pull-request-codecommit/commit/1a27e9d4d0048dd2d2e312e4dcdb19a95e4007ef))

* chore(deps-dev): bump pytest from 7.4.0 to 7.4.1 (#158) ([`750eea1`](https://github.com/conijnio/pull-request-codecommit/commit/750eea115231dafa284bbba4dae08fbb61636e22))

* chore(deps-dev): bump pytest from 7.4.0 to 7.4.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.0 to 7.4.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.4.0...7.4.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`90560a5`](https://github.com/conijnio/pull-request-codecommit/commit/90560a5e0ff4942ad2594c8315e049e8a62c2584))

* chore(deps): bump click from 8.1.6 to 8.1.7 (#156) ([`b25ff6f`](https://github.com/conijnio/pull-request-codecommit/commit/b25ff6fbbb8e605851de779aab3bd68ed62b7d90))

* chore(deps): bump click from 8.1.6 to 8.1.7

Bumps [click](https://github.com/pallets/click) from 8.1.6 to 8.1.7.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.6...8.1.7)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`2e2bdb9`](https://github.com/conijnio/pull-request-codecommit/commit/2e2bdb9a5abb3b98efcf04c1556ad7175119f666))

* chore(deps): bump click from 8.1.6 to 8.1.7 (#155) ([`fc4d9b6`](https://github.com/conijnio/pull-request-codecommit/commit/fc4d9b6386946aff480c01e69f29c5e2d71c7dde))

* chore(deps): bump click from 8.1.6 to 8.1.7

Bumps [click](https://github.com/pallets/click) from 8.1.6 to 8.1.7.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.6...8.1.7)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e038a25`](https://github.com/conijnio/pull-request-codecommit/commit/e038a25539be0a801507f3cc406fff26314d6004))

* chore(deps-dev): bump mypy from 1.5.0 to 1.5.1 (#154) ([`dfa34e1`](https://github.com/conijnio/pull-request-codecommit/commit/dfa34e1b847138c683230690176c506b69730bce))

* chore(deps-dev): bump mypy from 1.5.0 to 1.5.1

Bumps [mypy](https://github.com/python/mypy) from 1.5.0 to 1.5.1.
- [Commits](https://github.com/python/mypy/compare/v1.5.0...v1.5.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0e3777b`](https://github.com/conijnio/pull-request-codecommit/commit/0e3777bc993e5a7a6d4ade3773bcdf02f9a90bf8))

* chore(deps-dev): bump radon from 5.1.0 to 6.0.1 (#153) ([`ff9758d`](https://github.com/conijnio/pull-request-codecommit/commit/ff9758da2eacb4d7ecf6a24384605ea8989dbed5))

* chore(deps-dev): bump radon from 5.1.0 to 6.0.1

Bumps [radon](https://github.com/rubik/radon) from 5.1.0 to 6.0.1.
- [Changelog](https://github.com/rubik/radon/blob/master/CHANGELOG)
- [Commits](https://github.com/rubik/radon/compare/v5.1.0...v6.0.1)

---
updated-dependencies:
- dependency-name: radon
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`47f0297`](https://github.com/conijnio/pull-request-codecommit/commit/47f029704d9420d5e12fe74ae88f12c088adaab2))

* chore(deps-dev): bump xenon from 0.9.0 to 0.9.1 (#152) ([`fc1cfb5`](https://github.com/conijnio/pull-request-codecommit/commit/fc1cfb5084468b033429e47c7340bd0cf0b5e476))

* chore(deps-dev): bump xenon from 0.9.0 to 0.9.1

Bumps [xenon](https://github.com/rubik/xenon) from 0.9.0 to 0.9.1.
- [Changelog](https://github.com/rubik/xenon/blob/master/CHANGELOG)
- [Commits](https://github.com/rubik/xenon/compare/v0.9.0...v0.9.1)

---
updated-dependencies:
- dependency-name: xenon
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`daaae5c`](https://github.com/conijnio/pull-request-codecommit/commit/daaae5c769afbfb4ae291b288733e317589f3c74))

* chore(deps-dev): bump mypy from 1.4.1 to 1.5.0 (#151)

Bumps [mypy](https://github.com/python/mypy) from 1.4.1 to 1.5.0.
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/2ff7c0de571d434a9a1f82fa183d32fa32999b40&#34;&gt;&lt;code&gt;2ff7c0d&lt;/code&gt;&lt;/a&gt;
[release 1.5] stubtest: Fix &lt;code&gt;__mypy-replace&lt;/code&gt; false positives
(&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15689&#34;&gt;#15689&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15751&#34;&gt;#15751&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/373b73abeb14fdd1f3021f4c27fe1721d2986ed4&#34;&gt;&lt;code&gt;373b73a&lt;/code&gt;&lt;/a&gt;
[Release 1.5] Update typing_extensions stubs (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15745&#34;&gt;#15745&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/a6bd80ed8c91138ce6112b5ce71fc406d426cd01&#34;&gt;&lt;code&gt;a6bd80e&lt;/code&gt;&lt;/a&gt;
Remove &lt;code&gt;+dev&lt;/code&gt; from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/9dd0d396e0a8b477e4bf723a6a24d82db7785ea8&#34;&gt;&lt;code&gt;9dd0d39&lt;/code&gt;&lt;/a&gt;
Manually revert &amp;quot;Add support for attrs.fields (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15021&#34;&gt;#15021&lt;/a&gt;)&amp;quot;
(&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15674&#34;&gt;#15674&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/45e1bf7a83686a5b933eb009447e89e5d1c41ca9&#34;&gt;&lt;code&gt;45e1bf7&lt;/code&gt;&lt;/a&gt;
Typeshed cherry-pick: Fix &lt;a
href=&#34;https://github.com/patch&#34;&gt;&lt;code&gt;@​patch&lt;/code&gt;&lt;/a&gt; when
&lt;code&gt;new&lt;/code&gt; is missing (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/10459&#34;&gt;#10459&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15673&#34;&gt;#15673&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/7a9418356082092d2cb1585acb816b2074cff43e&#34;&gt;&lt;code&gt;7a94183&lt;/code&gt;&lt;/a&gt;
Fix dataclass/protocol crash on joining types (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15629&#34;&gt;#15629&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/2ebd51e881490f4d20635cde92ef9e3edbbad68c&#34;&gt;&lt;code&gt;2ebd51e&lt;/code&gt;&lt;/a&gt;
Teach &lt;code&gt;stubgen&lt;/code&gt; to work with &lt;code&gt;complex&lt;/code&gt; and unary
expressions (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15661&#34;&gt;#15661&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/39833810ddcd29561f3ffed44703380aa26a68be&#34;&gt;&lt;code&gt;3983381&lt;/code&gt;&lt;/a&gt;
Fix testLiteralMeets failure (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15659&#34;&gt;#15659&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/3bf85217386806b0f68bf8857b61379ae2f6ad1e&#34;&gt;&lt;code&gt;3bf8521&lt;/code&gt;&lt;/a&gt;
Consistently avoid type-checking unreachable code (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15386&#34;&gt;#15386&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/dfea43ff96976435ee5f37d1294cca792b8f26cf&#34;&gt;&lt;code&gt;dfea43f&lt;/code&gt;&lt;/a&gt;
Add error code &amp;quot;explicit-override&amp;quot; for strict &lt;a
href=&#34;https://github.com/override&#34;&gt;&lt;code&gt;@​override&lt;/code&gt;&lt;/a&gt; mode (PEP
698) (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15512&#34;&gt;#15512&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.4.1...v1.5.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.4.1&amp;new-version=1.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt; ([`8e25009`](https://github.com/conijnio/pull-request-codecommit/commit/8e250096cfe801abd92afd4c3140c75ff7c7eeba))

* chore(deps-dev): bump mypy from 1.4.1 to 1.5.0

Bumps [mypy](https://github.com/python/mypy) from 1.4.1 to 1.5.0.
- [Commits](https://github.com/python/mypy/compare/v1.4.1...v1.5.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`caacbbe`](https://github.com/conijnio/pull-request-codecommit/commit/caacbbe9b93fcef834730e60e7afbdcea159d2bd))

* chore: group dependencies and assign code owner ([`7625313`](https://github.com/conijnio/pull-request-codecommit/commit/76253133b49d891184061ae7c651a3e7c1039703))

* chore: fix auto-merge ([`73cf7b6`](https://github.com/conijnio/pull-request-codecommit/commit/73cf7b6d9c419713406b9decd08c68469b39e50d))

* chore(deps-dev): bump types-toml from 0.10.8.6 to 0.10.8.7 (#150) ([`fb24320`](https://github.com/conijnio/pull-request-codecommit/commit/fb24320dc2e000c3516d7900d989aedb75baa015))

* chore(deps-dev): bump types-toml from 0.10.8.6 to 0.10.8.7

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.8.6 to 0.10.8.7.
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e0e8661`](https://github.com/conijnio/pull-request-codecommit/commit/e0e86610b4b127a83a124c0e83001aed7978e14c))

* chore: change license to apache 2.0 ([`3f092a0`](https://github.com/conijnio/pull-request-codecommit/commit/3f092a093d612443f1b39737570eef346771b413))

* chore: enable auto-commit for dependabot pull requests (#149)

**Issue #, if available:**

## Description of changes:

&lt;!--- One or two sentences as a summary of what&#39;s being changed --&gt;

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [ ] Update tests
* [ ] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`c560b4b`](https://github.com/conijnio/pull-request-codecommit/commit/c560b4b64485a815763c1d38abd2cd50a7d31d4a))

* chore: enable auto-commit for dependabot pull requests ([`0e7d79b`](https://github.com/conijnio/pull-request-codecommit/commit/0e7d79b6fe163b6db46e5a3b85ca578dae82206e))

* chore(deps): bump click from 8.1.5 to 8.1.6 (#148) ([`dbb323c`](https://github.com/conijnio/pull-request-codecommit/commit/dbb323c64e4c720972cbc79be48c63cf6458aee4))

* chore(deps): bump click from 8.1.5 to 8.1.6

Bumps [click](https://github.com/pallets/click) from 8.1.5 to 8.1.6.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/8.1.6/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.5...8.1.6)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c647b94`](https://github.com/conijnio/pull-request-codecommit/commit/c647b9476ee547bef52f689ba6a59a6dfc359eb4))

* chore(deps): bump click from 8.1.5 to 8.1.6 (#147) ([`f5c6da0`](https://github.com/conijnio/pull-request-codecommit/commit/f5c6da04066244c8e83ee1c602c5b11331b9945a))

* chore(deps): bump click from 8.1.5 to 8.1.6

Bumps [click](https://github.com/pallets/click) from 8.1.5 to 8.1.6.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/8.1.6/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.5...8.1.6)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a771d81`](https://github.com/conijnio/pull-request-codecommit/commit/a771d819ab738fe54237cb72d516cf5d98450664))

* chore(deps): bump click from 8.1.4 to 8.1.5 (#146) ([`b6684d4`](https://github.com/conijnio/pull-request-codecommit/commit/b6684d459a60983743315a376baa5ce59ebdec66))

* chore(deps): bump click from 8.1.4 to 8.1.5

Bumps [click](https://github.com/pallets/click) from 8.1.4 to 8.1.5.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/8.1.5/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.4...8.1.5)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`482a58c`](https://github.com/conijnio/pull-request-codecommit/commit/482a58c9f50a307b2d1c30d38589937ef0c907e6))

* chore(deps): bump click from 8.1.4 to 8.1.5 (#145) ([`48a2a55`](https://github.com/conijnio/pull-request-codecommit/commit/48a2a55aec4f33b052249dc8ce278ba69fda4e32))

* chore(deps): bump click from 8.1.4 to 8.1.5

Bumps [click](https://github.com/pallets/click) from 8.1.4 to 8.1.5.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/8.1.5/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.4...8.1.5)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b64eed6`](https://github.com/conijnio/pull-request-codecommit/commit/b64eed6e6cfe7fba4a8ee98a9e1c0fc1ea04b1e8))

### Fix

* fix: release instructions ([`d101526`](https://github.com/conijnio/pull-request-codecommit/commit/d1015264f029ebf9e85231c745e78b0b278dfdb1))

### Unknown

* Update auto-merge.yml ([`04288a3`](https://github.com/conijnio/pull-request-codecommit/commit/04288a31449e233f1f95a2a648c7d1f6415e23e0))

* Update dependabot.yml ([`237923d`](https://github.com/conijnio/pull-request-codecommit/commit/237923d2507f52a21af67b7afb9ade9f2eeacf69))

* Update auto-merge.yml ([`3058314`](https://github.com/conijnio/pull-request-codecommit/commit/3058314125051a40609e4b2ece71d48b96fe0ab1))


## v0.5.3 (2023-07-11)

### Chore

* chore(deps): bump click from 8.1.3 to 8.1.4 (#143)

Bumps [click](https://github.com/pallets/click) from 8.1.3 to 8.1.4.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pallets/click/releases&#34;&gt;click&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;8.1.4&lt;/h2&gt;
&lt;p&gt;This is a fix release for the 8.1.x feature branch.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Changes: &lt;a
href=&#34;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-4&#34;&gt;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-4&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Milestone: &lt;a
href=&#34;https://github.com/pallets/click/milestone/19?closed=1&#34;&gt;https://github.com/pallets/click/milestone/19?closed=1&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pallets/click/blob/main/CHANGES.rst&#34;&gt;click&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;Version 8.1.4&lt;/h2&gt;
&lt;p&gt;Released 2023-07-06&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Replace all &lt;code&gt;typing.Dict&lt;/code&gt; occurrences to
&lt;code&gt;typing.MutableMapping&lt;/code&gt; for
parameter hints. :issue:&lt;code&gt;2255&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Improve type hinting for decorators and give all generic types
parameters.
:issue:&lt;code&gt;2398&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Fix return value and type signature of
&lt;code&gt;shell_completion.add_completion_class&lt;/code&gt;
function. :pr:&lt;code&gt;2421&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Bash version detection doesn&#39;t fail on Windows.
:issue:&lt;code&gt;2461&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Completion works if there is a dot (&lt;code&gt;.&lt;/code&gt;) in the program
name. :issue:&lt;code&gt;2166&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Improve type annotations for pyright type checker.
:issue:&lt;code&gt;2268&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Improve responsiveness of &lt;code&gt;click.clear()&lt;/code&gt;.
:issue:&lt;code&gt;2284&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Improve command name detection when using Shiv or PEX.
:issue:&lt;code&gt;2332&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Avoid showing empty lines if command help text is empty.
:issue:&lt;code&gt;2368&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;ZSH completion script works when loaded from &lt;code&gt;fpath&lt;/code&gt;.
:issue:&lt;code&gt;2344&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;EOFError&lt;/code&gt; and &lt;code&gt;KeyboardInterrupt&lt;/code&gt; tracebacks
are not suppressed when
&lt;code&gt;standalone_mode&lt;/code&gt; is disabled. :issue:&lt;code&gt;2380&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;@group.command&lt;/code&gt; does not fail if the group was created
with a custom
&lt;code&gt;command_class&lt;/code&gt;. :issue:&lt;code&gt;2416&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;multiple=True&lt;/code&gt; is allowed for flag options again and
does not require
setting &lt;code&gt;default=()&lt;/code&gt;. :issue:&lt;code&gt;2246, 2292,
2295&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Make the decorators returned by &lt;code&gt;@argument()&lt;/code&gt; and
&lt;code&gt;@option()&lt;/code&gt; reusable when the
&lt;code&gt;cls&lt;/code&gt; parameter is used. :issue:&lt;code&gt;2294&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Don&#39;t fail when writing filenames to streams with strict errors.
Replace invalid
bytes with the replacement character (&lt;code&gt;�&lt;/code&gt;).
:issue:&lt;code&gt;2395&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Remove unnecessary attempt to detect MSYS2 environment.
:issue:&lt;code&gt;2355&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Remove outdated and unnecessary detection of App Engine environment.
:pr:&lt;code&gt;2554&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;echo()&lt;/code&gt; does not fail when no streams are attached, such
as with &lt;code&gt;pythonw&lt;/code&gt; on
Windows. :issue:&lt;code&gt;2415&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Argument with &lt;code&gt;expose_value=False&lt;/code&gt; do not cause
completion to fail. :issue:&lt;code&gt;2336&lt;/code&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/3d873a3f567d1bbcb6fb25f0fbe3c3128488d99d&#34;&gt;&lt;code&gt;3d873a3&lt;/code&gt;&lt;/a&gt;
release version 8.1.4&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/dd691da8028a090657f081b584ce1efb1bb149d2&#34;&gt;&lt;code&gt;dd691da&lt;/code&gt;&lt;/a&gt;
use pypi trusted publisher auth&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/b67fe5f70a8c88bf54d6c7058b1154a81d32815c&#34;&gt;&lt;code&gt;b67fe5f&lt;/code&gt;&lt;/a&gt;
completion doesn&#39;t fail with &lt;code&gt;expose_value=False&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2556&#34;&gt;#2556&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/4cf7c6cdb10e441da775b4a3a7ee55caec83249e&#34;&gt;&lt;code&gt;4cf7c6c&lt;/code&gt;&lt;/a&gt;
completion works for expose_value=False&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/549947111c4af2191dd4b245e1de2c25d20c36d6&#34;&gt;&lt;code&gt;5499471&lt;/code&gt;&lt;/a&gt;
echo doesn&#39;t fail with no streams (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2555&#34;&gt;#2555&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/ecb99836a44367bad62960045d586e31e4a95766&#34;&gt;&lt;code&gt;ecb9983&lt;/code&gt;&lt;/a&gt;
echo doesn&#39;t fail with no streams&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/9a536eebd958558c2cd24c17fb66fac112f1ac91&#34;&gt;&lt;code&gt;9a536ee&lt;/code&gt;&lt;/a&gt;
remove msys2 and app engine detection (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2554&#34;&gt;#2554&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/daca3cfce4dcc98451362da0785e4db5fd2b1d8a&#34;&gt;&lt;code&gt;daca3cf&lt;/code&gt;&lt;/a&gt;
remove app engine detection&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/8f019ba54eb6838c182c8bfe9310a8d526602071&#34;&gt;&lt;code&gt;8f019ba&lt;/code&gt;&lt;/a&gt;
remove msys2 detection&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/af1e8d44d64181484a60dd63044da706bcc13439&#34;&gt;&lt;code&gt;af1e8d4&lt;/code&gt;&lt;/a&gt;
&lt;code&gt;format_filename&lt;/code&gt; replaces invalid bytes (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2553&#34;&gt;#2553&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pallets/click/compare/8.1.3...8.1.4&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=click&amp;package-manager=pip&amp;previous-version=8.1.3&amp;new-version=8.1.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt; ([`2cfbe3d`](https://github.com/conijnio/pull-request-codecommit/commit/2cfbe3dc1359c0aceae6ba930028903ea960c382))

* chore(deps): bump click from 8.1.3 to 8.1.4

Bumps [click](https://github.com/pallets/click) from 8.1.3 to 8.1.4.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.3...8.1.4)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`54a4da0`](https://github.com/conijnio/pull-request-codecommit/commit/54a4da03cb3e3662bc8488208b3ec946ed70a90b))

* chore(deps-dev): bump black from 23.3.0 to 23.7.0

Bumps [black](https://github.com/psf/black) from 23.3.0 to 23.7.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.3.0...23.7.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8018305`](https://github.com/conijnio/pull-request-codecommit/commit/80183053deaa0c8494d8bdbb047735dba7cb54eb))

* chore(deps): bump click from 8.1.3 to 8.1.4

Bumps [click](https://github.com/pallets/click) from 8.1.3 to 8.1.4.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.3...8.1.4)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8c07d89`](https://github.com/conijnio/pull-request-codecommit/commit/8c07d891837da847236bf857deea40c8b9bdae7c))

* chore(deps-dev): bump mypy from 1.4.0 to 1.4.1

Bumps [mypy](https://github.com/python/mypy) from 1.4.0 to 1.4.1.
- [Commits](https://github.com/python/mypy/compare/v1.4.0...v1.4.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`934f6d0`](https://github.com/conijnio/pull-request-codecommit/commit/934f6d0189c2cad4c444ed790ecbde335bd5b690))

* chore(deps-dev): bump pytest from 7.3.2 to 7.4.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.3.2 to 7.4.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.3.2...7.4.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e99f1ec`](https://github.com/conijnio/pull-request-codecommit/commit/e99f1ecef0123471a6e66d53dd7eec174979af16))

### Fix

* fix: ignore click decorator and remove unused main() call ([`c523046`](https://github.com/conijnio/pull-request-codecommit/commit/c523046e263fbf9b2ce394fe8d9c022342526547))

### Unknown

* Merge pull request #144 from Nr18/dependabot/pip/black-23.7.0 ([`1d8c04f`](https://github.com/conijnio/pull-request-codecommit/commit/1d8c04f6cf61bc3785ec4a57a7956da4a8bbe167))

* Merge pull request #142 from Nr18/dependabot/pip/click-8.1.4 ([`8424ce9`](https://github.com/conijnio/pull-request-codecommit/commit/8424ce99948db45e01d796ac3ec2072fa90ef185))

* Merge pull request #140 from Nr18/dependabot/pip/pytest-7.4.0 ([`5f0ade0`](https://github.com/conijnio/pull-request-codecommit/commit/5f0ade0a124074a28100a2226ecbe22ef1b59437))

* Merge pull request #141 from Nr18/dependabot/pip/mypy-1.4.1 ([`045a15a`](https://github.com/conijnio/pull-request-codecommit/commit/045a15a580a93c7d2430ec00849feae4bff4d7ec))

* Merge pull request #139 from Nr18/develop

release: develop to main branch ([`fc7ee5c`](https://github.com/conijnio/pull-request-codecommit/commit/fc7ee5c5ac4214eb5e4a24bbf38aaafddcd317e8))


## v0.5.2 (2023-06-21)

### Chore

* chore(deps-dev): bump mypy from 1.3.0 to 1.4.0

Bumps [mypy](https://github.com/python/mypy) from 1.3.0 to 1.4.0.
- [Commits](https://github.com/python/mypy/compare/v1.3.0...v1.4.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`bb365b0`](https://github.com/conijnio/pull-request-codecommit/commit/bb365b00c09433020ec2666af7bb45d57e5deee8))

* chore(deps-dev): bump pytest from 7.3.1 to 7.3.2

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.3.1 to 7.3.2.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.3.1...7.3.2)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`5c66e83`](https://github.com/conijnio/pull-request-codecommit/commit/5c66e83221b53ed38da5c79c54baaf096facfffa))

* chore(deps): bump cryptography from 39.0.2 to 41.0.0

Bumps [cryptography](https://github.com/pyca/cryptography) from 39.0.2 to 41.0.0.
- [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pyca/cryptography/compare/39.0.2...41.0.0)

---
updated-dependencies:
- dependency-name: cryptography
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b974d3f`](https://github.com/conijnio/pull-request-codecommit/commit/b974d3f33817ba81bcc022bedc8b4c4fac8f33df))

* chore(deps-dev): bump pytest-cov from 4.0.0 to 4.1.0

Bumps [pytest-cov](https://github.com/pytest-dev/pytest-cov) from 4.0.0 to 4.1.0.
- [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-cov/compare/v4.0.0...v4.1.0)

---
updated-dependencies:
- dependency-name: pytest-cov
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`2e92050`](https://github.com/conijnio/pull-request-codecommit/commit/2e920502c686af569a94943ad1c4853a8f484594))

* chore(deps): bump requests from 2.28.2 to 2.31.0

Bumps [requests](https://github.com/psf/requests) from 2.28.2 to 2.31.0.
- [Release notes](https://github.com/psf/requests/releases)
- [Changelog](https://github.com/psf/requests/blob/main/HISTORY.md)
- [Commits](https://github.com/psf/requests/compare/v2.28.2...v2.31.0)

---
updated-dependencies:
- dependency-name: requests
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a4c04e2`](https://github.com/conijnio/pull-request-codecommit/commit/a4c04e2209beaca637de35940cb4bd6050d89fa8))

* chore(deps-dev): bump mypy from 1.2.0 to 1.3.0

Bumps [mypy](https://github.com/python/mypy) from 1.2.0 to 1.3.0.
- [Commits](https://github.com/python/mypy/compare/v1.2.0...v1.3.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e4cb645`](https://github.com/conijnio/pull-request-codecommit/commit/e4cb645c3ec10d993af336d57a8d23900e588146))

* chore(deps-dev): bump pytest from 7.3.0 to 7.3.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.3.0 to 7.3.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.3.0...7.3.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`601d84d`](https://github.com/conijnio/pull-request-codecommit/commit/601d84df5f8e17528edf0ddbe04841700b31ab43))

* chore(deps-dev): bump pytest from 7.2.2 to 7.3.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.2.2 to 7.3.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.2.2...7.3.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`61336c0`](https://github.com/conijnio/pull-request-codecommit/commit/61336c00704f2d641e58f40e9c937ed91bdd01b7))

* chore(deps-dev): bump mypy from 1.1.1 to 1.2.0

Bumps [mypy](https://github.com/python/mypy) from 1.1.1 to 1.2.0.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v1.1.1...v1.2.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`aaf2d67`](https://github.com/conijnio/pull-request-codecommit/commit/aaf2d67b8a3298530c2fc34106b52cf7a7b9d45e))

* chore(deps-dev): bump mypy from 1.0.1 to 1.1.1

Bumps [mypy](https://github.com/python/mypy) from 1.0.1 to 1.1.1.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v1.0.1...v1.1.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a035d50`](https://github.com/conijnio/pull-request-codecommit/commit/a035d5097e44dd582874c9286ca4cd5924899589))

* chore(deps-dev): bump types-toml from 0.10.8.5 to 0.10.8.6

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.8.5 to 0.10.8.6.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a5057dc`](https://github.com/conijnio/pull-request-codecommit/commit/a5057dc802148b6e346ae72d09d162f1330dbef8))

* chore(deps-dev): bump black from 23.1.0 to 23.3.0

Bumps [black](https://github.com/psf/black) from 23.1.0 to 23.3.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.1.0...23.3.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f5ac630`](https://github.com/conijnio/pull-request-codecommit/commit/f5ac6308ffa83ea1b0d1a74a5527d814dd2ce22f))

### Fix

* fix: semantic versioning ([`8c49d5f`](https://github.com/conijnio/pull-request-codecommit/commit/8c49d5f37cf00b8f0762d26a07da62ec6306c848))

* fix: make target ([`a7c9f8e`](https://github.com/conijnio/pull-request-codecommit/commit/a7c9f8e061c5e8581692b61a6be6c009964daa5d))

### Unknown

* 0.5.1 ([`abc504f`](https://github.com/conijnio/pull-request-codecommit/commit/abc504f14c79aab892759068d69408e9a4b0ac29))

* Merge pull request #138 from Nr18/dependabot/pip/mypy-1.4.0

chore(deps-dev): bump mypy from 1.3.0 to 1.4.0 ([`91a49de`](https://github.com/conijnio/pull-request-codecommit/commit/91a49de388cc2a40fecfbe571daad97145c87bca))

* Merge pull request #137 from Nr18/dependabot/pip/pytest-7.3.2 ([`32623e9`](https://github.com/conijnio/pull-request-codecommit/commit/32623e932a0f110fa24164a1db229d6e6bff53bb))

* Merge pull request #136 from Nr18/dependabot/pip/cryptography-41.0.0 ([`7f5c383`](https://github.com/conijnio/pull-request-codecommit/commit/7f5c383799ba6f23b892decee86292ccd33d4827))

* Merge pull request #135 from Nr18/dependabot/pip/pytest-cov-4.1.0 ([`64f756f`](https://github.com/conijnio/pull-request-codecommit/commit/64f756f75ff5c973a30f16187d3048644b82ca28))

* Merge pull request #134 from Nr18/dependabot/pip/requests-2.31.0 ([`a18b802`](https://github.com/conijnio/pull-request-codecommit/commit/a18b8022199bc11833e64b45d4d4f038c76bc64f))

* Merge pull request #133 from Nr18/dependabot/pip/mypy-1.3.0

chore(deps-dev): bump mypy from 1.2.0 to 1.3.0 ([`7ad5f06`](https://github.com/conijnio/pull-request-codecommit/commit/7ad5f0611baf92cc0d8bb810bcb8a5c03689566a))

* Merge pull request #132 from Nr18/dependabot/pip/pytest-7.3.1 ([`e321b85`](https://github.com/conijnio/pull-request-codecommit/commit/e321b857a0ac9ed501949c82f8ef59181decef64))

* Merge pull request #131 from Nr18/dependabot/pip/pytest-7.3.0 ([`238eb04`](https://github.com/conijnio/pull-request-codecommit/commit/238eb0478bbd941a254eb7ee5f174fe1adee8a09))

* Merge pull request #130 from Nr18/dependabot/pip/mypy-1.2.0 ([`9eff046`](https://github.com/conijnio/pull-request-codecommit/commit/9eff046c9e8e08c3245f4a7029b1dc2f2ed3547b))

* Merge pull request #127 from Nr18/dependabot/pip/mypy-1.1.1 ([`acf0a29`](https://github.com/conijnio/pull-request-codecommit/commit/acf0a29f094e1e89e822e1393044b1befcdcd1b4))

* Merge branch &#39;develop&#39; into dependabot/pip/mypy-1.1.1 ([`12c3abb`](https://github.com/conijnio/pull-request-codecommit/commit/12c3abbb3ce17f77ef181179474a45ce36c83864))

* Merge pull request #129 from Nr18/dependabot/pip/types-toml-0.10.8.6 ([`5173bc6`](https://github.com/conijnio/pull-request-codecommit/commit/5173bc6254192cfa4768d2b900de090809cc4663))

* Merge branch &#39;develop&#39; into dependabot/pip/types-toml-0.10.8.6 ([`3ffe0c1`](https://github.com/conijnio/pull-request-codecommit/commit/3ffe0c16883de436e27110d8a67a36c3a12624a3))

* Merge pull request #128 from Nr18/dependabot/pip/black-23.3.0 ([`9903add`](https://github.com/conijnio/pull-request-codecommit/commit/9903add5a60f3c53dfe1d2f982a25e6c5bf08a09))


## v0.5.1 (2023-03-06)

### Chore

* chore: remove deprecated functionality (#125)

**Issue #, if available:** N/A

## Description of changes:

Replace deprecated functionality with the newer version.

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`dd774aa`](https://github.com/conijnio/pull-request-codecommit/commit/dd774aad427bc7df0936717d7365dace126237cc))

### Unknown

* Merge pull request #126 from Nr18/develop

chore: remove deprecated functionality (#125) ([`61fb602`](https://github.com/conijnio/pull-request-codecommit/commit/61fb602f34d512e2935e3f32401e7988b7ed0986))


## v0.5.0 (2023-03-06)

### Chore

* chore: version bump ([`4139f04`](https://github.com/conijnio/pull-request-codecommit/commit/4139f04b1a315efd4681e37962d8892fa39cd921))

* chore(deps-dev): bump pytest from 7.2.1 to 7.2.2

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.2.1 to 7.2.2.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.2.1...7.2.2)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`777349a`](https://github.com/conijnio/pull-request-codecommit/commit/777349a542e533e19147beb8a96e9ed2dbd93ad6))

* chore(deps-dev): bump types-toml from 0.10.8.4 to 0.10.8.5

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.8.4 to 0.10.8.5.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`db27ad5`](https://github.com/conijnio/pull-request-codecommit/commit/db27ad52dad5c23f6ab07736cc67c0a9e31f7e31))

* chore(deps-dev): bump mypy from 1.0.0 to 1.0.1

Bumps [mypy](https://github.com/python/mypy) from 1.0.0 to 1.0.1.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v1.0.0...v1.0.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c859e70`](https://github.com/conijnio/pull-request-codecommit/commit/c859e707a9925dedf7c70587f10de0a5ecc4825b))

* chore(deps-dev): bump types-toml from 0.10.8.3 to 0.10.8.4

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.8.3 to 0.10.8.4.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`2e084b5`](https://github.com/conijnio/pull-request-codecommit/commit/2e084b5142a928d8197adc59e0c28af604ad2dcb))

* chore(deps): bump cryptography from 39.0.0 to 39.0.1

Bumps [cryptography](https://github.com/pyca/cryptography) from 39.0.0 to 39.0.1.
- [Release notes](https://github.com/pyca/cryptography/releases)
- [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pyca/cryptography/compare/39.0.0...39.0.1)

---
updated-dependencies:
- dependency-name: cryptography
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c9a94eb`](https://github.com/conijnio/pull-request-codecommit/commit/c9a94ebd188ef4ebad714ef7a7ec5d90118377f2))

* chore(deps-dev): bump mypy from 0.991 to 1.0.0

Bumps [mypy](https://github.com/python/mypy) from 0.991 to 1.0.0.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.991...v1.0.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`acc10dd`](https://github.com/conijnio/pull-request-codecommit/commit/acc10dd08b7db914f54a6a4b5cf6e222b29611da))

* chore(deps-dev): bump types-toml from 0.10.8.2 to 0.10.8.3

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.8.2 to 0.10.8.3.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`23d50d8`](https://github.com/conijnio/pull-request-codecommit/commit/23d50d85cf842b101f6bfdb357b711ef264193a3))

* chore(deps-dev): bump types-toml from 0.10.8.1 to 0.10.8.2

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.8.1 to 0.10.8.2.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`df273bd`](https://github.com/conijnio/pull-request-codecommit/commit/df273bd9e278fa9cb6b83518c4f4c703208c7bd8))

* chore(deps-dev): bump black from 22.12.0 to 23.1.0

Bumps [black](https://github.com/psf/black) from 22.12.0 to 23.1.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.12.0...23.1.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`08a582c`](https://github.com/conijnio/pull-request-codecommit/commit/08a582c89a481801c3bffb74fa338338d307c11a))

* chore: update poetry and update poetry lock ([`6154216`](https://github.com/conijnio/pull-request-codecommit/commit/61542169729c1d136feed72f63032da8821bc614))

* chore(deps): bump future from 0.18.2 to 0.18.3

Bumps [future](https://github.com/PythonCharmers/python-future) from 0.18.2 to 0.18.3.
- [Release notes](https://github.com/PythonCharmers/python-future/releases)
- [Changelog](https://github.com/PythonCharmers/python-future/blob/master/docs/changelog.rst)
- [Commits](https://github.com/PythonCharmers/python-future/compare/v0.18.2...v0.18.3)

---
updated-dependencies:
- dependency-name: future
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7aff529`](https://github.com/conijnio/pull-request-codecommit/commit/7aff529b6bbdd0a14b3d1828ef88123b5ad6e25b))

* chore(deps-dev): bump pytest-mypy from 0.10.2 to 0.10.3

Bumps [pytest-mypy](https://github.com/dbader/pytest-mypy) from 0.10.2 to 0.10.3.
- [Release notes](https://github.com/dbader/pytest-mypy/releases)
- [Changelog](https://github.com/realpython/pytest-mypy/blob/main/changelog.md)
- [Commits](https://github.com/dbader/pytest-mypy/compare/v0.10.2...v0.10.3)

---
updated-dependencies:
- dependency-name: pytest-mypy
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ddb1a2d`](https://github.com/conijnio/pull-request-codecommit/commit/ddb1a2d0b6ea26e9cd959bb52d1c2d523f987556))

* chore(deps): bump certifi from 2021.10.8 to 2022.12.7

Bumps [certifi](https://github.com/certifi/python-certifi) from 2021.10.8 to 2022.12.7.
- [Release notes](https://github.com/certifi/python-certifi/releases)
- [Commits](https://github.com/certifi/python-certifi/compare/2021.10.08...2022.12.07)

---
updated-dependencies:
- dependency-name: certifi
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f828734`](https://github.com/conijnio/pull-request-codecommit/commit/f828734a3ce95def681013c40ff983189a29231c))

* chore(deps-dev): bump black from 22.10.0 to 22.12.0

Bumps [black](https://github.com/psf/black) from 22.10.0 to 22.12.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.10.0...22.12.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9b14825`](https://github.com/conijnio/pull-request-codecommit/commit/9b148251aaa9e9d1dc992d10b9cf363b14478bf5))

* chore(deps-dev): bump pytest-mypy from 0.10.1 to 0.10.2

Bumps [pytest-mypy](https://github.com/dbader/pytest-mypy) from 0.10.1 to 0.10.2.
- [Release notes](https://github.com/dbader/pytest-mypy/releases)
- [Changelog](https://github.com/realpython/pytest-mypy/blob/main/changelog.md)
- [Commits](https://github.com/dbader/pytest-mypy/compare/v0.10.1...v0.10.2)

---
updated-dependencies:
- dependency-name: pytest-mypy
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7d62e3c`](https://github.com/conijnio/pull-request-codecommit/commit/7d62e3ca935954612be4c6e367d205ace1684915))

* chore(deps-dev): bump twine from 4.0.1 to 4.0.2

Bumps [twine](https://github.com/pypa/twine) from 4.0.1 to 4.0.2.
- [Release notes](https://github.com/pypa/twine/releases)
- [Changelog](https://github.com/pypa/twine/blob/main/docs/changelog.rst)
- [Commits](https://github.com/pypa/twine/compare/4.0.1...4.0.2)

---
updated-dependencies:
- dependency-name: twine
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`413f4cf`](https://github.com/conijnio/pull-request-codecommit/commit/413f4cf79b87641806c9736359ca995cb9028f88))

* chore(deps-dev): bump mypy from 0.990 to 0.991

Bumps [mypy](https://github.com/python/mypy) from 0.990 to 0.991.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.990...v0.991)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7d1f6a2`](https://github.com/conijnio/pull-request-codecommit/commit/7d1f6a2a21adaed6dc9cef41a62a4cb2b4ed5e70))

* chore(deps-dev): bump types-toml from 0.10.8 to 0.10.8.1

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.8 to 0.10.8.1.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`10f342b`](https://github.com/conijnio/pull-request-codecommit/commit/10f342bdc6744abd7f94a48fbfce1618fc012bff))

* chore(deps-dev): bump pytest-mypy from 0.10.0 to 0.10.1

Bumps [pytest-mypy](https://github.com/dbader/pytest-mypy) from 0.10.0 to 0.10.1.
- [Release notes](https://github.com/dbader/pytest-mypy/releases)
- [Changelog](https://github.com/realpython/pytest-mypy/blob/main/changelog.md)
- [Commits](https://github.com/dbader/pytest-mypy/compare/v0.10.0...v0.10.1)

---
updated-dependencies:
- dependency-name: pytest-mypy
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8e54b3b`](https://github.com/conijnio/pull-request-codecommit/commit/8e54b3b21578ea7b4fe057a1955c4d83e1ff2b21))

* chore(deps-dev): bump mypy from 0.982 to 0.990

Bumps [mypy](https://github.com/python/mypy) from 0.982 to 0.990.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.982...v0.990)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f557035`](https://github.com/conijnio/pull-request-codecommit/commit/f55703591dd5a091fddab399015da1e6599f71ac))

* chore(deps-dev): bump black from 22.8.0 to 22.10.0

Bumps [black](https://github.com/psf/black) from 22.8.0 to 22.10.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.8.0...22.10.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`41ab22d`](https://github.com/conijnio/pull-request-codecommit/commit/41ab22d7618239db49dcfa999f77333fabe122e4))

* chore(deps-dev): bump pytest from 7.1.3 to 7.2.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.1.3 to 7.2.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.1.3...7.2.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`210bd7f`](https://github.com/conijnio/pull-request-codecommit/commit/210bd7f81d779a2c82573649e67180efbb90eade))

* chore(deps-dev): bump mypy from 0.981 to 0.982

Bumps [mypy](https://github.com/python/mypy) from 0.981 to 0.982.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.981...v0.982)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`59e6d6a`](https://github.com/conijnio/pull-request-codecommit/commit/59e6d6a571c8db542ab8eb5b636e37710513dcd1))

* chore(deps-dev): bump pytest-cov from 3.0.0 to 4.0.0

Bumps [pytest-cov](https://github.com/pytest-dev/pytest-cov) from 3.0.0 to 4.0.0.
- [Release notes](https://github.com/pytest-dev/pytest-cov/releases)
- [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-cov/compare/v3.0.0...v4.0.0)

---
updated-dependencies:
- dependency-name: pytest-cov
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`15f40f4`](https://github.com/conijnio/pull-request-codecommit/commit/15f40f45bf99b514a91de52bbf336bc3d4ef8565))

* chore(deps-dev): bump pytest-mypy from 0.9.1 to 0.10.0

Bumps [pytest-mypy](https://github.com/dbader/pytest-mypy) from 0.9.1 to 0.10.0.
- [Release notes](https://github.com/dbader/pytest-mypy/releases)
- [Changelog](https://github.com/dbader/pytest-mypy/blob/master/changelog.md)
- [Commits](https://github.com/dbader/pytest-mypy/compare/v0.9.1...v0.10.0)

---
updated-dependencies:
- dependency-name: pytest-mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3c1834a`](https://github.com/conijnio/pull-request-codecommit/commit/3c1834afe47232c037611bc3913aefdd4d76814f))

* chore(deps-dev): bump mypy from 0.971 to 0.981

Bumps [mypy](https://github.com/python/mypy) from 0.971 to 0.981.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.971...v0.981)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b9b16b7`](https://github.com/conijnio/pull-request-codecommit/commit/b9b16b7fe7fa423f49196370a4d537f9414b5288))

* chore(deps-dev): bump pytest from 7.1.2 to 7.1.3

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.1.2 to 7.1.3.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.1.2...7.1.3)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`dcdb39c`](https://github.com/conijnio/pull-request-codecommit/commit/dcdb39c78d26b0718c6e4792b1d1015fe4aa823f))

* chore(deps-dev): bump black from 22.6.0 to 22.8.0

Bumps [black](https://github.com/psf/black) from 22.6.0 to 22.8.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.6.0...22.8.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7df6fbf`](https://github.com/conijnio/pull-request-codecommit/commit/7df6fbfb3e9f7833a6f81777341e5fe1253d4770))

* chore(deps-dev): bump mypy from 0.961 to 0.971

Bumps [mypy](https://github.com/python/mypy) from 0.961 to 0.971.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.961...v0.971)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8304d3b`](https://github.com/conijnio/pull-request-codecommit/commit/8304d3bc0c4274fedbaed07d66bc7b0430149afa))

* chore(deps-dev): bump types-toml from 0.10.7 to 0.10.8

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.7 to 0.10.8.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8ae7437`](https://github.com/conijnio/pull-request-codecommit/commit/8ae7437339fb0b998b300425c4e846d070b76244))

### Fix

* fix: use specific poetry version (#123)

**Issue #, if available:** N/A

## Description of changes:

By specifying the exact poetry version we prevent local vs remote
differences.

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`89936d2`](https://github.com/conijnio/pull-request-codecommit/commit/89936d2d9b1541681c6d8194b1549f1dcb04b8f7))

### Unknown

* Merge pull request #124 from Nr18/develop

fix: use specific poetry version (#123) ([`860d524`](https://github.com/conijnio/pull-request-codecommit/commit/860d524bdbf4a8ba98000c5e83febe557dcf911e))

* Merge pull request #122 from Nr18/develop

release: 0.5.0 ([`e03ef09`](https://github.com/conijnio/pull-request-codecommit/commit/e03ef09828ef11c41a741cd28cc09fabf62ef246))

* Merge pull request #121 from Nr18/chore/release

chore: version bump ([`140f4a9`](https://github.com/conijnio/pull-request-codecommit/commit/140f4a9d94500b5eba879604b75aca7b190c0a0a))

* Merge pull request #120 from Nr18/dependabot/pip/pytest-7.2.2

chore(deps-dev): bump pytest from 7.2.1 to 7.2.2 ([`48a42da`](https://github.com/conijnio/pull-request-codecommit/commit/48a42da7d63fcb3563103b7d522789af91137b40))

* Merge pull request #119 from Nr18/dependabot/pip/types-toml-0.10.8.5 ([`e5fa5b8`](https://github.com/conijnio/pull-request-codecommit/commit/e5fa5b8609b541222878939fbc34d3b13003a818))

* Merge pull request #118 from Nr18/dependabot/pip/mypy-1.0.1 ([`341cdf2`](https://github.com/conijnio/pull-request-codecommit/commit/341cdf2a40ee33384fde57cf7d68bf77e40e1e7e))

* Merge pull request #117 from Nr18/dependabot/pip/types-toml-0.10.8.4 ([`2d8a268`](https://github.com/conijnio/pull-request-codecommit/commit/2d8a26890fbaddcbe89f6377f65d61a65899d4cb))

* Merge pull request #116 from Nr18/dependabot/pip/cryptography-39.0.1 ([`c197873`](https://github.com/conijnio/pull-request-codecommit/commit/c197873ed9ca0d41c1ff10c734a1ee39b85250b7))

* Merge pull request #115 from Nr18/dependabot/pip/mypy-1.0.0

chore(deps-dev): bump mypy from 0.991 to 1.0.0 ([`867fddd`](https://github.com/conijnio/pull-request-codecommit/commit/867fddd9a88f71bdd6aea99e86412f6108517a3f))

* Merge branch &#39;develop&#39; into dependabot/pip/mypy-1.0.0 ([`431691d`](https://github.com/conijnio/pull-request-codecommit/commit/431691d8c2d31ba966725bbec95261753c0e7e47))

* Merge pull request #114 from Nr18/dependabot/pip/types-toml-0.10.8.3

chore(deps-dev): bump types-toml from 0.10.8.2 to 0.10.8.3 ([`31411eb`](https://github.com/conijnio/pull-request-codecommit/commit/31411eb0adcc1aa46c894c5ec632fb0614742a7e))

* Merge pull request #113 from Nr18/dependabot/pip/types-toml-0.10.8.2 ([`9fadbef`](https://github.com/conijnio/pull-request-codecommit/commit/9fadbefee0eaf7dd8dff55d9157b75a4c77dc00e))

* Merge pull request #112 from Nr18/dependabot/pip/black-23.1.0 ([`c10eef4`](https://github.com/conijnio/pull-request-codecommit/commit/c10eef40c3c5cfb4dac5c19ffe9f4127359e3dde))

* Merge pull request #111 from Nr18/dependabot/pip/future-0.18.3

chore(deps): bump future from 0.18.2 to 0.18.3 ([`8a3888d`](https://github.com/conijnio/pull-request-codecommit/commit/8a3888d3200972e79e1606337092484d1c361d8d))

* Merge pull request #109 from Nr18/dependabot/pip/pytest-mypy-0.10.3 ([`28d046e`](https://github.com/conijnio/pull-request-codecommit/commit/28d046e2ec11fa4240c001d836d238b7242743ad))

* Merge pull request #107 from Nr18/dependabot/pip/certifi-2022.12.7

chore(deps): bump certifi from 2021.10.8 to 2022.12.7 ([`5f03ab5`](https://github.com/conijnio/pull-request-codecommit/commit/5f03ab5c6c0ddd53341095f2cef201ca9e246c0a))

* Merge pull request #108 from Nr18/dependabot/pip/black-22.12.0 ([`8781b61`](https://github.com/conijnio/pull-request-codecommit/commit/8781b619741a1704b1ae08ba75b75643d85b899d))

* Merge pull request #105 from Nr18/dependabot/pip/pytest-mypy-0.10.2

chore(deps-dev): bump pytest-mypy from 0.10.1 to 0.10.2 ([`1f25bf9`](https://github.com/conijnio/pull-request-codecommit/commit/1f25bf936d4f7d6e4460ddbcd7d2b7f62d09ff99))

* Merge pull request #106 from Nr18/dependabot/pip/twine-4.0.2

chore(deps-dev): bump twine from 4.0.1 to 4.0.2 ([`d7d332d`](https://github.com/conijnio/pull-request-codecommit/commit/d7d332d63a5fc544681b1b0f3b9386d093dc0ec6))

* Merge pull request #104 from Nr18/dependabot/pip/mypy-0.991 ([`47c93cf`](https://github.com/conijnio/pull-request-codecommit/commit/47c93cf2b239103a500c34c5e4e201b9880760e9))

* Merge pull request #103 from Nr18/dependabot/pip/types-toml-0.10.8.1 ([`dc61e71`](https://github.com/conijnio/pull-request-codecommit/commit/dc61e71a298f768ab9eaee60d7aa8c40107181b5))

* Merge pull request #102 from Nr18/dependabot/pip/pytest-mypy-0.10.1 ([`27ecd21`](https://github.com/conijnio/pull-request-codecommit/commit/27ecd21addae4eeb497c0015513c99c372f628b6))

* Merge pull request #101 from Nr18/dependabot/pip/mypy-0.990

chore(deps-dev): bump mypy from 0.982 to 0.990 ([`da38763`](https://github.com/conijnio/pull-request-codecommit/commit/da387634c18fc920506b4c28b668b099d4246b9e))

* Merge pull request #99 from Nr18/dependabot/pip/black-22.10.0

chore(deps-dev): bump black from 22.8.0 to 22.10.0 ([`5694878`](https://github.com/conijnio/pull-request-codecommit/commit/5694878120e0e6fbb8b667b04a74ce907518bf4a))

* Merge pull request #100 from Nr18/dependabot/pip/pytest-7.2.0 ([`35f7af9`](https://github.com/conijnio/pull-request-codecommit/commit/35f7af9299bafea3681a79bf4cf12a818ba4ed10))

* Merge pull request #98 from Nr18/dependabot/pip/mypy-0.982 ([`990e97f`](https://github.com/conijnio/pull-request-codecommit/commit/990e97f3a2acceadbc29fd822693f7e133fdd0c6))

* Merge pull request #97 from Nr18/dependabot/pip/pytest-cov-4.0.0 ([`f4f615c`](https://github.com/conijnio/pull-request-codecommit/commit/f4f615cec3836439e22dad80460e67cd8c48adc4))

* Merge pull request #96 from Nr18/dependabot/pip/pytest-mypy-0.10.0 ([`eb0063e`](https://github.com/conijnio/pull-request-codecommit/commit/eb0063e28702338f1c476357a6e5c5568ee4ad76))

* Merge pull request #95 from Nr18/dependabot/pip/mypy-0.981 ([`74367e7`](https://github.com/conijnio/pull-request-codecommit/commit/74367e75af9e2efc8b717c50d0848317a8255a41))

* Merge pull request #93 from Nr18/dependabot/pip/black-22.8.0

chore(deps-dev): bump black from 22.6.0 to 22.8.0 ([`023a930`](https://github.com/conijnio/pull-request-codecommit/commit/023a930cd836ce776326d18a731615e04d70c651))

* Merge branch &#39;develop&#39; into dependabot/pip/black-22.8.0 ([`4c49e33`](https://github.com/conijnio/pull-request-codecommit/commit/4c49e33aa2e4eaa64414d7efdcb80e531de92446))

* Merge pull request #94 from Nr18/dependabot/pip/pytest-7.1.3

chore(deps-dev): bump pytest from 7.1.2 to 7.1.3 ([`ea33aec`](https://github.com/conijnio/pull-request-codecommit/commit/ea33aec8b4df811ef3c2c430c8fb288243143c9a))

* Merge pull request #92 from Nr18/dependabot/pip/mypy-0.971 ([`2288fd9`](https://github.com/conijnio/pull-request-codecommit/commit/2288fd9bd2eef9982b389d88ce6bd636ab840b8a))

* Merge pull request #91 from Nr18/dependabot/pip/types-toml-0.10.8

chore(deps-dev): bump types-toml from 0.10.7 to 0.10.8 ([`14525fe`](https://github.com/conijnio/pull-request-codecommit/commit/14525fe92874e0dcd6d7c060c119293ade78f85f))


## v0.4.3 (2022-07-11)

### Chore

* chore: version bump ([`97c3bb6`](https://github.com/conijnio/pull-request-codecommit/commit/97c3bb6ab5863b204219af35c523422daffeb16f))

* chore(deps-dev): bump black from 22.3.0 to 22.6.0

Bumps [black](https://github.com/psf/black) from 22.3.0 to 22.6.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.3.0...22.6.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1759abd`](https://github.com/conijnio/pull-request-codecommit/commit/1759abd0f0087d117b2b8f2c735d5db8cbe795aa))

* chore(deps-dev): bump mypy from 0.950 to 0.961

Bumps [mypy](https://github.com/python/mypy) from 0.950 to 0.961.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.950...v0.961)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`53d9e8b`](https://github.com/conijnio/pull-request-codecommit/commit/53d9e8bceb4e262361ba1a92b60693d5a7838c5e))

* chore(deps-dev): bump twine from 4.0.0 to 4.0.1

Bumps [twine](https://github.com/pypa/twine) from 4.0.0 to 4.0.1.
- [Release notes](https://github.com/pypa/twine/releases)
- [Changelog](https://github.com/pypa/twine/blob/main/docs/changelog.rst)
- [Commits](https://github.com/pypa/twine/compare/4.0.0...4.0.1)

---
updated-dependencies:
- dependency-name: twine
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6f90ac2`](https://github.com/conijnio/pull-request-codecommit/commit/6f90ac22e181a4e892f53dc4eb96d202b44c8789))

* chore(deps-dev): bump types-toml from 0.10.6 to 0.10.7

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.6 to 0.10.7.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`06e7369`](https://github.com/conijnio/pull-request-codecommit/commit/06e736981aaa30b4c1270396e05e47c5edddaa30))

* chore(deps): bump click from 8.1.2 to 8.1.3

Bumps [click](https://github.com/pallets/click) from 8.1.2 to 8.1.3.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.2...8.1.3)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b1d43df`](https://github.com/conijnio/pull-request-codecommit/commit/b1d43dfa7b300335f113118a901d5435b0afe467))

* chore(deps): bump click from 8.1.2 to 8.1.3

Bumps [click](https://github.com/pallets/click) from 8.1.2 to 8.1.3.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.2...8.1.3)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`86a699a`](https://github.com/conijnio/pull-request-codecommit/commit/86a699a357590b5e9a92bfe7ba3a8d9c0ca774f0))

* chore(deps-dev): bump mypy from 0.942 to 0.950

Bumps [mypy](https://github.com/python/mypy) from 0.942 to 0.950.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.942...v0.950)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`129e1a2`](https://github.com/conijnio/pull-request-codecommit/commit/129e1a21a1310783735ee850ec1e9c5268169011))

* chore(deps-dev): bump types-toml from 0.10.5 to 0.10.6

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.5 to 0.10.6.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`405d23f`](https://github.com/conijnio/pull-request-codecommit/commit/405d23f88fb6ebaed4acacf2a43158dab465ac96))

* chore(deps-dev): bump pytest from 7.1.1 to 7.1.2

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.1.1 to 7.1.2.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.1.1...7.1.2)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6fc49c0`](https://github.com/conijnio/pull-request-codecommit/commit/6fc49c0233a45bcf61fc0bb34f3b001484103f5e))

* chore(deps-dev): bump types-toml from 0.10.4 to 0.10.5

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.4 to 0.10.5.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`bbd18ef`](https://github.com/conijnio/pull-request-codecommit/commit/bbd18ef2e5a909c63787d6c258ad5bda32b1ea77))

* chore(deps): bump click from 8.0.4 to 8.1.2

Bumps [click](https://github.com/pallets/click) from 8.0.4 to 8.1.2.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.4...8.1.2)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a5c2181`](https://github.com/conijnio/pull-request-codecommit/commit/a5c2181cf7ffaf33a1660dff3a4fa69a0b385ef5))

* chore(deps): bump click from 8.0.4 to 8.1.2

Bumps [click](https://github.com/pallets/click) from 8.0.4 to 8.1.2.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.4...8.1.2)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3947098`](https://github.com/conijnio/pull-request-codecommit/commit/394709857672e761c609d3f64f766693e1f3c430))

* chore(deps-dev): bump twine from 3.8.0 to 4.0.0

Bumps [twine](https://github.com/pypa/twine) from 3.8.0 to 4.0.0.
- [Release notes](https://github.com/pypa/twine/releases)
- [Changelog](https://github.com/pypa/twine/blob/main/docs/changelog.rst)
- [Commits](https://github.com/pypa/twine/compare/3.8.0...4.0.0)

---
updated-dependencies:
- dependency-name: twine
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`24d0b72`](https://github.com/conijnio/pull-request-codecommit/commit/24d0b72598e73cc4d1ac4faf2a8fd36d64b50a01))

* chore(deps): bump click from 8.0.4 to 8.1.1

Bumps [click](https://github.com/pallets/click) from 8.0.4 to 8.1.1.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.4...8.1.1)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`52f9016`](https://github.com/conijnio/pull-request-codecommit/commit/52f901629a8ebfd94027ff89a358db2ccd2c8c48))

* chore(deps): bump click from 8.0.4 to 8.1.0

Bumps [click](https://github.com/pallets/click) from 8.0.4 to 8.1.0.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.4...8.1.0)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`061f90f`](https://github.com/conijnio/pull-request-codecommit/commit/061f90f61a487c3eddbc1509e3d07d0403351b97))

* chore(deps-dev): bump black from 22.1.0 to 22.3.0

Bumps [black](https://github.com/psf/black) from 22.1.0 to 22.3.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.1.0...22.3.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`15986d9`](https://github.com/conijnio/pull-request-codecommit/commit/15986d949c8ff39c2fd891d6806aeee1b1fa5384))

* chore(deps-dev): bump mypy from 0.941 to 0.942

Bumps [mypy](https://github.com/python/mypy) from 0.941 to 0.942.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.941...v0.942)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`04581f2`](https://github.com/conijnio/pull-request-codecommit/commit/04581f2e21afa175b7e338ae69b2b95303e4b240))

* chore(deps-dev): bump pytest from 7.1.0 to 7.1.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.1.0 to 7.1.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.1.0...7.1.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1278538`](https://github.com/conijnio/pull-request-codecommit/commit/12785382e05affc8e731c1750c21676c5a82d318))

* chore(deps-dev): bump mypy from 0.940 to 0.941

Bumps [mypy](https://github.com/python/mypy) from 0.940 to 0.941.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.940...v0.941)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`92bc332`](https://github.com/conijnio/pull-request-codecommit/commit/92bc332c08e4274bd01768624f15d78e8c6d6556))

* chore(deps-dev): bump xenon from 0.8.0 to 0.9.0

Bumps [xenon](https://github.com/rubik/xenon) from 0.8.0 to 0.9.0.
- [Release notes](https://github.com/rubik/xenon/releases)
- [Changelog](https://github.com/rubik/xenon/blob/master/CHANGELOG)
- [Commits](https://github.com/rubik/xenon/compare/v0.8.0...v0.9.0)

---
updated-dependencies:
- dependency-name: xenon
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`cedc6df`](https://github.com/conijnio/pull-request-codecommit/commit/cedc6dfd90125357056227c4d9559079d3a17d79))

* chore(deps-dev): bump pytest from 7.0.1 to 7.1.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.0.1 to 7.1.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.0.1...7.1.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0d0464f`](https://github.com/conijnio/pull-request-codecommit/commit/0d0464f446dfdc56f530e3195ba1525e0f99731a))

* chore(deps-dev): bump mypy from 0.931 to 0.940

Bumps [mypy](https://github.com/python/mypy) from 0.931 to 0.940.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.931...v0.940)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`af33d36`](https://github.com/conijnio/pull-request-codecommit/commit/af33d3666e244a8db81aa5a1de5dc2144c4b7ba3))

### Unknown

* Merge pull request #90 from Nr18/develop

release: 0.4.3 ([`0444c1e`](https://github.com/conijnio/pull-request-codecommit/commit/0444c1e167efe165e7ade9f8cd0534530064fac5))

* Merge pull request #89 from Nr18/chore/version-bump

chore: version bump ([`9894a49`](https://github.com/conijnio/pull-request-codecommit/commit/9894a494256fa178e8ccc45a457c0e92444f0adb))

* Merge pull request #88 from Nr18/dependabot/pip/black-22.6.0 ([`05a7587`](https://github.com/conijnio/pull-request-codecommit/commit/05a75870b5b0edff446e2fa90556b192c4a0d1f8))

* Merge pull request #87 from Nr18/dependabot/pip/mypy-0.961

chore(deps-dev): bump mypy from 0.950 to 0.961 ([`f9b13b6`](https://github.com/conijnio/pull-request-codecommit/commit/f9b13b62e3894fc672b85e13eaf8231eacf8d446))

* Merge pull request #86 from Nr18/dependabot/pip/twine-4.0.1 ([`6390c09`](https://github.com/conijnio/pull-request-codecommit/commit/6390c099e193596ca1b51d4476fb3c560124f6ce))

* Merge pull request #84 from Nr18/dependabot/pip/types-toml-0.10.7 ([`e4015a5`](https://github.com/conijnio/pull-request-codecommit/commit/e4015a57620b75b7aedecb6d924ffc7883ba8de3))

* Merge pull request #83 from Nr18/dependabot/pip/click-8.1.3 ([`0bdec60`](https://github.com/conijnio/pull-request-codecommit/commit/0bdec606635f1535493716725350f875d6d4c9e5))

* Merge pull request #82 from Nr18/dependabot/pip/click-8.1.3 ([`071fcb4`](https://github.com/conijnio/pull-request-codecommit/commit/071fcb469f8b69e1431bf3af521310e7e533df72))

* Merge pull request #81 from Nr18/dependabot/pip/mypy-0.950 ([`21bcd52`](https://github.com/conijnio/pull-request-codecommit/commit/21bcd52b42832984283de67597c5918a7ee00148))

* Merge pull request #80 from Nr18/dependabot/pip/types-toml-0.10.6 ([`5af3ea8`](https://github.com/conijnio/pull-request-codecommit/commit/5af3ea87103889aa744aebc62e50bc3bdd05ed3e))

* Merge pull request #79 from Nr18/dependabot/pip/pytest-7.1.2 ([`120c562`](https://github.com/conijnio/pull-request-codecommit/commit/120c562fa290c59524b69c283d53d0a1c3735516))

* Merge pull request #78 from Nr18/dependabot/pip/types-toml-0.10.5 ([`9dd972e`](https://github.com/conijnio/pull-request-codecommit/commit/9dd972e3826733aed210fc0446c0f80277f12fb7))

* Merge pull request #77 from Nr18/dependabot/pip/click-8.1.2 ([`646a757`](https://github.com/conijnio/pull-request-codecommit/commit/646a7573b4ea802b94ff84c1292ef6af82ebe9d5))

* Merge pull request #76 from Nr18/dependabot/pip/click-8.1.2 ([`302ec95`](https://github.com/conijnio/pull-request-codecommit/commit/302ec95b9584153887fde6893af3652d57d747a3))

* Merge pull request #75 from Nr18/dependabot/pip/twine-4.0.0 ([`a1410a5`](https://github.com/conijnio/pull-request-codecommit/commit/a1410a5510ae5b118c175972a2611eeca0ffbe89))

* Merge pull request #74 from Nr18/dependabot/pip/click-8.1.1 ([`d3403a9`](https://github.com/conijnio/pull-request-codecommit/commit/d3403a9c75c201c191f20e7448f8746df0e2b7f9))

* Merge pull request #72 from Nr18/dependabot/pip/click-8.1.0 ([`2c0d9e0`](https://github.com/conijnio/pull-request-codecommit/commit/2c0d9e04485c93c84197d8fb92238f3ad12347cc))

* Merge pull request #71 from Nr18/dependabot/pip/black-22.3.0 ([`bd2255a`](https://github.com/conijnio/pull-request-codecommit/commit/bd2255aebffd6a808235734b4d27a26e62859eb9))

* Merge pull request #70 from Nr18/dependabot/pip/mypy-0.942 ([`cd2982f`](https://github.com/conijnio/pull-request-codecommit/commit/cd2982fd14fed096f11eb1492d4035394bb5a976))

* Merge pull request #69 from Nr18/dependabot/pip/pytest-7.1.1 ([`5cba8a3`](https://github.com/conijnio/pull-request-codecommit/commit/5cba8a3d83c097b557c06a554646202951358647))

* Merge pull request #68 from Nr18/dependabot/pip/mypy-0.941

chore(deps-dev): bump mypy from 0.940 to 0.941 ([`c756f0b`](https://github.com/conijnio/pull-request-codecommit/commit/c756f0ba58feb19e0fe72cf12f92f2a782037f80))

* Merge pull request #65 from Nr18/dependabot/pip/xenon-0.9.0

chore(deps-dev): bump xenon from 0.8.0 to 0.9.0 ([`d895c79`](https://github.com/conijnio/pull-request-codecommit/commit/d895c790279682ebe76e434784a5b0c27a64441a))

* Merge pull request #67 from Nr18/dependabot/pip/pytest-7.1.0

chore(deps-dev): bump pytest from 7.0.1 to 7.1.0 ([`22ef168`](https://github.com/conijnio/pull-request-codecommit/commit/22ef168606fcccc073908a4b871bd2494a04b0f4))

* Merge pull request #66 from Nr18/dependabot/pip/mypy-0.940

chore(deps-dev): bump mypy from 0.931 to 0.940 ([`30e4132`](https://github.com/conijnio/pull-request-codecommit/commit/30e41321c843b5df814d189ccb600a1973a0c759))


## v0.4.2 (2022-02-21)

### Chore

* chore: version bump ([`fcf534a`](https://github.com/conijnio/pull-request-codecommit/commit/fcf534a779f6cac8cdffc6987605f1dbc1e8853d))

* chore(deps-dev): bump black from 21.12b0 to 22.1.0

Bumps [black](https://github.com/psf/black) from 21.12b0 to 22.1.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/commits/22.1.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8f0aedf`](https://github.com/conijnio/pull-request-codecommit/commit/8f0aedf857a1da294507643f451f865d31def02d))

* chore(deps-dev): bump pytest from 6.2.5 to 7.0.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.2.5 to 7.0.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/6.2.5...7.0.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ac1ec38`](https://github.com/conijnio/pull-request-codecommit/commit/ac1ec387e526fb645fefb537b5c1182c293f712c))

* chore(deps): bump click from 8.0.3 to 8.0.4

Bumps [click](https://github.com/pallets/click) from 8.0.3 to 8.0.4.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.3...8.0.4)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b914a42`](https://github.com/conijnio/pull-request-codecommit/commit/b914a42f2d60ff8c764e4a3d159af7bed5278820))

### Fix

* fix: push all commits to the remote

Before we compare the two remote branches we first need to push all commits to the remote. ([`5752ef1`](https://github.com/conijnio/pull-request-codecommit/commit/5752ef1987527f90b3df4ad120317aa48f207824))

### Unknown

* Merge pull request #64 from Nr18/develop

chore: release v0.4.2 ([`6b77e5e`](https://github.com/conijnio/pull-request-codecommit/commit/6b77e5eafa89dcaa9f07c205ac5c2a432a72fa9b))

* Merge pull request #63 from Nr18/chore/version-bump

chore: version bump ([`21f6406`](https://github.com/conijnio/pull-request-codecommit/commit/21f6406f0e15174fb4f8b6977fd0994c6d22f907))

* Merge pull request #62 from Nr18/fix/push-before-compare

fix: push all commits to the remote ([`8da6b47`](https://github.com/conijnio/pull-request-codecommit/commit/8da6b477f49988fb4a0d12a58e48e754530e0949))

* Merge pull request #60 from Nr18/dependabot/pip/black-22.1.0

chore(deps-dev): bump black from 21.12b0 to 22.1.0 ([`807ea19`](https://github.com/conijnio/pull-request-codecommit/commit/807ea19298f53424669303b999bb7fa81760d1f9))

* Merge pull request #61 from Nr18/dependabot/pip/pytest-7.0.1

chore(deps-dev): bump pytest from 6.2.5 to 7.0.1 ([`738d66b`](https://github.com/conijnio/pull-request-codecommit/commit/738d66b1066733c99b5d0192cd0b2b910688bd24))

* Merge pull request #59 from Nr18/dependabot/pip/click-8.0.4 ([`2c6b7a1`](https://github.com/conijnio/pull-request-codecommit/commit/2c6b7a11ea0434ff80d9d9eaebb8700d06bc18a4))


## v0.4.1 (2022-02-20)

### Chore

* chore: label the dependabot pull requests

Dependabot uses a chore(deps-dev) prefix. Because the colon was included in the regex this did not match. ([`04c5d4e`](https://github.com/conijnio/pull-request-codecommit/commit/04c5d4e1ce0cb8907d4be8918e0828e97170f4bb))

* chore(deps-dev): bump types-toml from 0.10.3 to 0.10.4

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.3 to 0.10.4.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c4fd3fe`](https://github.com/conijnio/pull-request-codecommit/commit/c4fd3fe09194b1baab6d74889e9746100ca13350))

* chore(deps-dev): bump mypy from 0.910 to 0.931

Bumps [mypy](https://github.com/python/mypy) from 0.910 to 0.931.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.910...v0.931)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`cb7b3a6`](https://github.com/conijnio/pull-request-codecommit/commit/cb7b3a6676c7d76dd962811dce53d2767318eea6))

* chore(deps): bump click from 8.0.3 to 8.0.4

Bumps [click](https://github.com/pallets/click) from 8.0.3 to 8.0.4.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.3...8.0.4)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1a8feef`](https://github.com/conijnio/pull-request-codecommit/commit/1a8feefbd82811a704db75ffed108d55d807b8e2))

* chore(deps-dev): bump pytest-mypy from 0.8.1 to 0.9.1

Bumps [pytest-mypy](https://github.com/dbader/pytest-mypy) from 0.8.1 to 0.9.1.
- [Release notes](https://github.com/dbader/pytest-mypy/releases)
- [Changelog](https://github.com/dbader/pytest-mypy/blob/master/changelog.md)
- [Commits](https://github.com/dbader/pytest-mypy/compare/v0.8.1...v0.9.1)

---
updated-dependencies:
- dependency-name: pytest-mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1043702`](https://github.com/conijnio/pull-request-codecommit/commit/1043702fff08b6b85bbbc57a2d1d3f3f0f5f8594))

* chore(deps-dev): bump twine from 3.7.1 to 3.8.0

Bumps [twine](https://github.com/pypa/twine) from 3.7.1 to 3.8.0.
- [Release notes](https://github.com/pypa/twine/releases)
- [Changelog](https://github.com/pypa/twine/blob/main/docs/changelog.rst)
- [Commits](https://github.com/pypa/twine/compare/3.7.1...3.8.0)

---
updated-dependencies:
- dependency-name: twine
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7955c78`](https://github.com/conijnio/pull-request-codecommit/commit/7955c7801b45bbc4ebcdae03a5fd7951fa04fdf7))

* chore: install dependabot

Keep all dependencies up to date by installing dependant. ([`613701b`](https://github.com/conijnio/pull-request-codecommit/commit/613701bb99499b39e9aa8d290c7123444f840c36))

* chore: add code of conduct

In order to get the project fully setup. We add the default code of conduct. ([`04fc553`](https://github.com/conijnio/pull-request-codecommit/commit/04fc55321feb7359e78497b637d548b58ebf8c63))

* chore: version bump ([`d918ae4`](https://github.com/conijnio/pull-request-codecommit/commit/d918ae4787f83327c1980573e27546d95f59d494))

* chore: remove test shell script

The shell script was useful in the beginning. Now it lost it&#39;s value as we depend on a remote. ([`ed8b6e6`](https://github.com/conijnio/pull-request-codecommit/commit/ed8b6e6e92a6ba03ebe288fead7641c57287bd98))

### Documentation

* docs: remove deprecated command

We prefer the `git pr` syntax over calling the executable directly. For this reason we remove the references to the executable. ([`124b4d3`](https://github.com/conijnio/pull-request-codecommit/commit/124b4d3d1b33c516f17f65aa2da6533077d92d9d))

### Fix

* fix: mark dependabot updates as dependencies ([`c8077ae`](https://github.com/conijnio/pull-request-codecommit/commit/c8077ae7536e936ca178d22d689dfd119df8fa32))

* fix: use separate category ([`fff0bb4`](https://github.com/conijnio/pull-request-codecommit/commit/fff0bb4b77c944955ec08edb0e58db3a572ec98b))

* fix: handling of aws and git failures

By catching the stderr and error codes from the aws and git executions we render a proper error message.

Issue: #26 ([`522ae56`](https://github.com/conijnio/pull-request-codecommit/commit/522ae5692a80451b3cb09bd61f28d5c61fa2e1a8))

### Unknown

* Merge pull request #58 from Nr18/develop

chore: release 0.4.1 ([`0d93519`](https://github.com/conijnio/pull-request-codecommit/commit/0d935191701d36a55cae4338332dbdf71504fc7a))

* Merge pull request #57 from Nr18/chore/label-dependabot

fix: mark dependabot updates as dependencies ([`88f7b79`](https://github.com/conijnio/pull-request-codecommit/commit/88f7b7970b93539ab75ccf55a23bf52da9426ba9))

* Merge branch &#39;develop&#39; into chore/label-dependabot ([`9e113c3`](https://github.com/conijnio/pull-request-codecommit/commit/9e113c305f1b3a38bd843dd5c12e19d09d547898))

* Merge pull request #55 from Nr18/dependabot/pip/click-8.0.4

chore(deps): bump click from 8.0.3 to 8.0.4 ([`7ef1404`](https://github.com/conijnio/pull-request-codecommit/commit/7ef14043945d51e6e1f6b0d3bbb1180b4a0c85c7))

* Merge branch &#39;develop&#39; into dependabot/pip/click-8.0.4 ([`dbce368`](https://github.com/conijnio/pull-request-codecommit/commit/dbce36863a8125755a475483e1d43879bd466f09))

* Merge pull request #54 from Nr18/dependabot/pip/mypy-0.931

chore(deps-dev): bump mypy from 0.910 to 0.931 ([`42e220b`](https://github.com/conijnio/pull-request-codecommit/commit/42e220b6d8787f2c6bdc46816949cb48403008a5))

* Merge branch &#39;develop&#39; into dependabot/pip/mypy-0.931 ([`a8686e1`](https://github.com/conijnio/pull-request-codecommit/commit/a8686e16d07bb5ab474cf8e38894e4aee92711b6))

* Merge pull request #53 from Nr18/dependabot/pip/types-toml-0.10.4

chore(deps-dev): bump types-toml from 0.10.3 to 0.10.4 ([`1883ea6`](https://github.com/conijnio/pull-request-codecommit/commit/1883ea614044eed719e631892aa7b75c38cd42b6))

* Merge branch &#39;develop&#39; into dependabot/pip/types-toml-0.10.4 ([`f211ff1`](https://github.com/conijnio/pull-request-codecommit/commit/f211ff1d73cce1862e6e532cc7c93010baaecdf3))

* Merge pull request #56 from Nr18/chore/label-dependabot

chore: label the dependabot pull requests ([`2477b0c`](https://github.com/conijnio/pull-request-codecommit/commit/2477b0c0e0e8534b73a65da2b38ada706d48f419))

* Merge branch &#39;develop&#39; into chore/label-dependabot ([`9b43dcc`](https://github.com/conijnio/pull-request-codecommit/commit/9b43dcc58485461b370ca529fc6b0d3f48710e74))

* Merge branch &#39;develop&#39; into dependabot/pip/click-8.0.4 ([`3e1f0a0`](https://github.com/conijnio/pull-request-codecommit/commit/3e1f0a0be0a38c4222b061798766c0dd5b406f42))

* Merge branch &#39;develop&#39; into dependabot/pip/mypy-0.931 ([`2abf67f`](https://github.com/conijnio/pull-request-codecommit/commit/2abf67ffbbf1c1aa36bd9de3ab1d30da426edd25))

* Merge branch &#39;develop&#39; into dependabot/pip/types-toml-0.10.4 ([`a7c93e3`](https://github.com/conijnio/pull-request-codecommit/commit/a7c93e308a07702af5564a7381608683db74b526))

* Merge pull request #52 from Nr18/dependabot/pip/pytest-mypy-0.9.1

chore(deps-dev): bump pytest-mypy from 0.8.1 to 0.9.1 ([`10e7424`](https://github.com/conijnio/pull-request-codecommit/commit/10e742423900a05b5f3eea98090463ad99c6325d))

* Merge branch &#39;develop&#39; into dependabot/pip/pytest-mypy-0.9.1 ([`7f44a2a`](https://github.com/conijnio/pull-request-codecommit/commit/7f44a2a4bb36ea4f9f36f2a8f40856109eaa1394))

* Merge pull request #51 from Nr18/dependabot/pip/twine-3.8.0

chore(deps-dev): bump twine from 3.7.1 to 3.8.0 ([`7f82afe`](https://github.com/conijnio/pull-request-codecommit/commit/7f82afecfbf22202d720dcd781ebd25110394f21))

* Merge pull request #50 from Nr18/chore/install-dependabot

chore: install dependabot ([`8d00cb9`](https://github.com/conijnio/pull-request-codecommit/commit/8d00cb96c2056de75025ced9d4622af322763032))

* Merge branch &#39;develop&#39; into chore/install-dependabot ([`abba00e`](https://github.com/conijnio/pull-request-codecommit/commit/abba00ec625ac607cb284dd599f54cc2c73e7051))

* Merge pull request #49 from Nr18/chore/add-code-of-conduct

chore: add code of conduct ([`d6509f1`](https://github.com/conijnio/pull-request-codecommit/commit/d6509f110f9f9878975fef27163a1b1edd53f4fd))

* Merge pull request #48 from Nr18/chore/version-bump

chore: version bump ([`3a53073`](https://github.com/conijnio/pull-request-codecommit/commit/3a53073f38b184916c276aae8c9c2932f140d819))

* Merge pull request #47 from Nr18/chore/cleanup

chore: remove test shell script ([`d654c29`](https://github.com/conijnio/pull-request-codecommit/commit/d654c29d26e474e55e6c9a119701ceca7d1e2337))

* Merge pull request #46 from Nr18/docs/update-readme

docs: remove deprecated command ([`d67bab8`](https://github.com/conijnio/pull-request-codecommit/commit/d67bab883b6397ed221d0836e9c935a2d7769bf3))

* Merge remote-tracking branch &#39;origin/develop&#39; into docs/update-readme ([`29cbbc3`](https://github.com/conijnio/pull-request-codecommit/commit/29cbbc3ff6008c7c819131d1b1ecf5773b8781df))

* Merge pull request #45 from Nr18/fix/execute-failures

fix: handling of aws and git failures ([`9fb20be`](https://github.com/conijnio/pull-request-codecommit/commit/9fb20bef77371cb783a67d6164445dfa5cd6cfa0))

* Merge branch &#39;develop&#39; into fix/execute-failures ([`db50f33`](https://github.com/conijnio/pull-request-codecommit/commit/db50f333afbe15354d109ece01a0707b4ce9f4ed))


## v0.4.0 (2022-02-20)

### Chore

* chore: version bump ([`5ff1b4d`](https://github.com/conijnio/pull-request-codecommit/commit/5ff1b4d97b81df857c3386d5dc32822eed0e85de))

* chore: automatically update the release body

Use the release drafter output to set the release notes automatically. ([`ba78a4e`](https://github.com/conijnio/pull-request-codecommit/commit/ba78a4efc0c3f86999ebfe23220e453a5a15d1f9))

### Documentation

* docs: update documentation ([`9352957`](https://github.com/conijnio/pull-request-codecommit/commit/93529575d4b2855a5bd53651b743a8e344a6d2e7))

### Feature

* feat: implement as a git sub-command

By exposing the package as `git-pr` we are able to call it as `git pr`. This is a nice UX improvement. ([`5d22e4f`](https://github.com/conijnio/pull-request-codecommit/commit/5d22e4fc5f2a8072951fbb10c25b4264256081f3))

### Unknown

* Merge pull request #44 from Nr18/develop

chore: release 0.4.0 ([`227515b`](https://github.com/conijnio/pull-request-codecommit/commit/227515b582a65e9c58822ddf494a8a24b90cf9a9))

* Merge pull request #43 from Nr18/chore/version-bump

chore: version bump ([`b038143`](https://github.com/conijnio/pull-request-codecommit/commit/b0381438378f53d24048992c751e1d7dfb053c14))

* Merge branch &#39;develop&#39; into chore/version-bump ([`9956801`](https://github.com/conijnio/pull-request-codecommit/commit/995680189cbcc0200ab6cffafa0c63407a612d55))

* Merge pull request #42 from Nr18/chore/release-notes

chore: automatically update the release body ([`5519903`](https://github.com/conijnio/pull-request-codecommit/commit/5519903aea81420d43f5d50f63744b64440648d0))

* Merge pull request #41 from Nr18/feat/git-implementation ([`539406c`](https://github.com/conijnio/pull-request-codecommit/commit/539406cb594b56292a903aa550b018e81d509361))


## v0.3.2 (2022-02-19)

### Chore

* chore: version bump ([`331d0bf`](https://github.com/conijnio/pull-request-codecommit/commit/331d0bf62f74e6bb0a5b9b886176d0bf2c6832f7))

### Documentation

* docs: describe the update process

Not everybody knows how to update python packages. This is the reason for adding the instructions to the main README.md. ([`358d4de`](https://github.com/conijnio/pull-request-codecommit/commit/358d4de3a06d8052db7c93e5e0c0d48e03f8e80b))

### Fix

* fix: compare remote branches

In the previous release (#34) we compared the remote destination. This works fine but we should compare both repos based on the remote. The pull request is created remote so the pull request description should reflect the remote state.

Issue: #32, #34 ([`ee2a135`](https://github.com/conijnio/pull-request-codecommit/commit/ee2a1350200caba6c089c7b3b8d96096f9f9583e))

### Unknown

* Merge pull request #40 from Nr18/develop

Release 0.3.2 ([`5c8594b`](https://github.com/conijnio/pull-request-codecommit/commit/5c8594b7678ae66bfd7c991a3b587fe9c9e8e1c0))

* Merge pull request #39 from Nr18/chore/version-bump

chore: version bump ([`d4dcc4d`](https://github.com/conijnio/pull-request-codecommit/commit/d4dcc4dc9cbb88ad0c411744520af384e7f0d194))

* Merge pull request #38 from Nr18/fix/compare-origin

fix: compare remote branches ([`d111c2d`](https://github.com/conijnio/pull-request-codecommit/commit/d111c2d38196780fa8759dc79851ee014c165488))

* Merge pull request #37 from Nr18/docs/upgrade-instructions

docs: describe the update process ([`4a92af7`](https://github.com/conijnio/pull-request-codecommit/commit/4a92af74b747a7ae66e014ae3b20a6cf1a241347))

* Merge branch &#39;develop&#39; into docs/upgrade-instructions ([`540a731`](https://github.com/conijnio/pull-request-codecommit/commit/540a731414ee337e1e56d29aa3ac5c3ae22d601b))


## v0.3.1 (2022-02-19)

### Chore

* chore: version bump ([`a9cca28`](https://github.com/conijnio/pull-request-codecommit/commit/a9cca28d1b892f5763444138892143366c3a9dcc))

### Fix

* fix: outdated local branch

When you create a pull request and the local version is behind of the remote. You got a pull request proposal with all already merged changes. By using the remote branch we prevent this.

Issue: #32 ([`17f07bb`](https://github.com/conijnio/pull-request-codecommit/commit/17f07bb6429c62d88f934f68b2d6867c33787b01))

* fix: delete the remote branch when pull request is merged

When we auto-merge a pull request we should also cleanup the existing remote branch.

Issue: #31 ([`bea4a91`](https://github.com/conijnio/pull-request-codecommit/commit/bea4a91662013a5eee02cca13778b43f2885a6a2))

### Unknown

* Merge pull request #36 from Nr18/develop

Release 0.3.1 ([`0d1327b`](https://github.com/conijnio/pull-request-codecommit/commit/0d1327ba068bc05ab5f8498242c8b861f388ca7d))

* Merge pull request #35 from Nr18/chore/version-bump

chore: version bump ([`7f9a46b`](https://github.com/conijnio/pull-request-codecommit/commit/7f9a46bd7506444298c1301d4496def644a81c97))

* Merge branch &#39;develop&#39; into chore/version-bump ([`6919eec`](https://github.com/conijnio/pull-request-codecommit/commit/6919eece021a7501c41f596618210455196c9c9c))

* Merge pull request #34 from Nr18/fix/outdated-local-branch

fix: outdated local branch ([`08cabc1`](https://github.com/conijnio/pull-request-codecommit/commit/08cabc13ed452d0b9aacfd592e0446fb36c595c7))

* Merge pull request #33 from Nr18/fix/remove-remote-branch

fix: delete the remote branch when pull request is merged ([`d16cb0e`](https://github.com/conijnio/pull-request-codecommit/commit/d16cb0ed495316670f0a0445341a00c2b2012f07))

* Merge branch &#39;develop&#39; into fix/remove-remote-branch ([`117661f`](https://github.com/conijnio/pull-request-codecommit/commit/117661f2bd37722ecf6776ea160018e12aa25eac))


## v0.3.0 (2022-02-10)

### Chore

* chore: version bump ([`45756d9`](https://github.com/conijnio/pull-request-codecommit/commit/45756d92fd94b186bd4e6879a3e6afa3d22ef490))

### Documentation

* docs: remove development note ([`549f3ff`](https://github.com/conijnio/pull-request-codecommit/commit/549f3ff4da15a8f34fc03e48d06e5a1d92207125))

* docs: update readme

Issue: #3 ([`add3293`](https://github.com/conijnio/pull-request-codecommit/commit/add3293cf25b8ba4b42de28661af710b074d33ea))

* docs: update readme

Issue: #21 ([`9225b1c`](https://github.com/conijnio/pull-request-codecommit/commit/9225b1c6f9a809098c1e943f875c005b9db8c613))

* docs: update readme to include the auto-merge feature ([`da01202`](https://github.com/conijnio/pull-request-codecommit/commit/da012026bfc41ac13661002360a879608067318f))

### Feature

* feat: allow branch overwrite

In some cases you want to overwrite the target branch. By supplying the `--branch my-branch` option you are now able to do just that.

Issue: #23 ([`6dd7445`](https://github.com/conijnio/pull-request-codecommit/commit/6dd7445cfc1c316debf86595cbd24e584a051a3b))

* feat: update the existing pull request

When a pull request creation is triggered, we need to check if their is not already a pull request open. When a pull request is open we should update the description.

Issue: #3 ([`19c43ea`](https://github.com/conijnio/pull-request-codecommit/commit/19c43eaa2209611ff0c088bf8caae24e560b3cd6))

* feat: delete working branch and pull destination

When you use the `--auto-merge` flag. We can cleanup the working branch and pull the merged result. This will remove some commands that you need to type.

Issue: #21 ([`0a3509e`](https://github.com/conijnio/pull-request-codecommit/commit/0a3509e7da85f989ab64378d7fe95026dfdb55e0))

* feat: implement auto-merge feature

Automatically merge the created pull request when the `--auto-merge` option is given.

Issue: #18 ([`7565a0f`](https://github.com/conijnio/pull-request-codecommit/commit/7565a0fafe4c5f09f422f4e90b0be31f6d6247cb))

### Fix

* fix: move title check ([`62a3ef2`](https://github.com/conijnio/pull-request-codecommit/commit/62a3ef2b4aaa789d1713a4b07877679e633f8ec7))

* fix: use correct command

Previously I used the merge branch command, this command requires different parameters and failed. By using the pull request merge action we fixed the behaviour. ([`13d641b`](https://github.com/conijnio/pull-request-codecommit/commit/13d641b51c3ce649751918c92c67cb5730f202e4))

### Refactor

* refactor: move pull request proposal to separate class ([`57337ee`](https://github.com/conijnio/pull-request-codecommit/commit/57337ee54f35f9b3e80f918184437f86dc0f8984))

* refactor: move codecommit repository logic

Move the logic that understands how to read pull requests from codecommit ([`04661e0`](https://github.com/conijnio/pull-request-codecommit/commit/04661e0772ad030fa4000682b76a2cfe3828cb6c))

* refactor: generate test data for each cli parameter that we support ([`bee8914`](https://github.com/conijnio/pull-request-codecommit/commit/bee891462dece970beaee747e8b8b3a4825b21c5))

* refactor: prepare codebase for auto-merge feature (#19)

* refactor: simplify the cli interaction
* refactor: encapsulate pull request information
* refactor: move pull request creation ([`16c0421`](https://github.com/conijnio/pull-request-codecommit/commit/16c04213e0cabb86cea20cd2f097941c36fd40eb))

### Unknown

* Merge pull request #29 from Nr18/develop

Release v0.3.0 ([`c601f08`](https://github.com/conijnio/pull-request-codecommit/commit/c601f08ef73e6279cd61585db69f3759c8513876))

* Merge pull request #30 from Nr18/chore/version-bump

chore: version bump ([`1c4b105`](https://github.com/conijnio/pull-request-codecommit/commit/1c4b105e5ace25f4564099d3f83d9f8820a99c9b))

* Merge pull request #28 from Nr18/feat/overwrite-branch

feat: allow branch overwrite ([`9f7beb6`](https://github.com/conijnio/pull-request-codecommit/commit/9f7beb6f635d6b9dd954051c4ee89c559b894e5c))

* Merge pull request #27 from Nr18/docs/remove-development-note

docs: remove development note ([`56c5d6d`](https://github.com/conijnio/pull-request-codecommit/commit/56c5d6de3daaf3c6f977800c0b066f65a2219e93))

* Merge pull request #25 from Nr18/feat/update-existing-pr

feat: update the existing pull request ([`797394e`](https://github.com/conijnio/pull-request-codecommit/commit/797394e4b54b3978ffbce2550e8308190771c2c2))

* Merge pull request #24 from Nr18/refactor/move-responsibility

refactor: move responsibilities ([`a03d02c`](https://github.com/conijnio/pull-request-codecommit/commit/a03d02ce3262581eef13c742c51ef21c3d755ed3))

* Merge pull request #22 from Nr18/feat/delete-branch

feat: delete working branch and pull destination ([`0a4f01d`](https://github.com/conijnio/pull-request-codecommit/commit/0a4f01dcbf6de5f1b960af93f7a8011258c8bc8e))

* Merge pull request #20 from Nr18/feat/auto-merge

feat: implement auto-merge feature ([`3ba156a`](https://github.com/conijnio/pull-request-codecommit/commit/3ba156ae64ab49de2c7afbfbc7293e691e4686d9))


## v0.2.0 (2022-01-27)

### Chore

* chore: version bump (#16) ([`fda47da`](https://github.com/conijnio/pull-request-codecommit/commit/fda47dacdb8a74fb904bc83a247c681a5ae164a4))

### Feature

* feat: use full description when we only have 1 commit (#15)

When you have a single commit. The body might contain additional information. So we include that information in the description as a suggestion. ([`970ae39`](https://github.com/conijnio/pull-request-codecommit/commit/970ae398ac0bc4371b44db0ca05b2e2a1d1bb932))

* feat: always push changes (#14)

By always pushing the changes before we create the pull request. We ensure that all changes are in Code Commit before we create the pull request.

Issue: #2 ([`603baa7`](https://github.com/conijnio/pull-request-codecommit/commit/603baa735dbf7ff2954d7698e6c5734ce485d9d4))

### Fix

* fix: repo name remote contains profile (#13)

When the remote contains a profile it was appended to the repository name. This was caused by #11.

Issue: #11 ([`7443e7a`](https://github.com/conijnio/pull-request-codecommit/commit/7443e7a4890fa4078ec526abeddd5768d2f23a91))

* fix: support fallback to default profile and region (#11)

* fix: support fallback to default profile and region

By moving the remote logic to its own class it allows us to encapsulate the behaviour. And making it easier to extend the behaviour.
Support both `codecommit://` and `codecommit::://` notations.

Fixes issue #7 ([`52389cc`](https://github.com/conijnio/pull-request-codecommit/commit/52389cc9e2a069b140ee87559378a6c3e753bf56))

* fix: index error when there are no commits (#9)

By returning a None when there are no commits we can detect gracefully.

Fixes Issue: #8 ([`5b87e37`](https://github.com/conijnio/pull-request-codecommit/commit/5b87e377bd204666330c568349a055bcd19f6c7b))

### Refactor

* refactor: introduce pull request class (#10)

By using an object it makes the code easier to read. It also moves the logic to create pull request proposals to its own class.

Issue: #8 ([`e15ccf9`](https://github.com/conijnio/pull-request-codecommit/commit/e15ccf9f5ae02e931f4bdb264e53da2164400ca2))

### Unknown

* Merge pull request #17 from Nr18/develop

Release v0.2.0 ([`c888e1d`](https://github.com/conijnio/pull-request-codecommit/commit/c888e1d0b328068c885f9a23e435bb93a053a246))


## v0.1.0 (2022-01-24)

### Chore

* chore: version bump (#4) ([`1afe0e3`](https://github.com/conijnio/pull-request-codecommit/commit/1afe0e3f85908548859ed4bd6186681a7b95dcc3))

### Documentation

* docs: remove docker documentation (#5)

Remove the docker documentation that was copied when I initially setup the repository. ([`9059558`](https://github.com/conijnio/pull-request-codecommit/commit/90595583315a4c6dc0065b451de4bce6f9fa7949))

### Feature

* feat: initial implementation (#1)

This is the initial implementation that we will use to test the tool out. ([`4c31f33`](https://github.com/conijnio/pull-request-codecommit/commit/4c31f33b39d327b33f662deca86133d28dbc4bab))

### Unknown

* Merge pull request #6 from Nr18/develop

chore: create release ([`1286343`](https://github.com/conijnio/pull-request-codecommit/commit/1286343d31ac022d52a821cee8498f44aa65329e))


## v0.0.1 (2022-01-21)

### Chore

* chore: initial commit ([`2f91eb0`](https://github.com/conijnio/pull-request-codecommit/commit/2f91eb0ea3ddf0ab8a7b085d498d3a61734b879b))
