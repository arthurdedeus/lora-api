#  (2022-05-07)


### Bug Fixes

* Add a minimum requirement version to urllib3 ([6471a51](https://github.com/arthurdedeus/lora-api/commit/6471a518abc8caa93b13839741e224f15a4565bb))
* Add missing celery tags to import ([b62f2b5](https://github.com/arthurdedeus/lora-api/commit/b62f2b5348c1124aea0e64e12d0323eed3b986dc))
* Add Socials tags on accounts views. ([a4d67f4](https://github.com/arthurdedeus/lora-api/commit/a4d67f4bb4120e8d4725e7426f82a372fb614a45))
* Bump django version to 2.2.8 ([1578ece](https://github.com/arthurdedeus/lora-api/commit/1578ece125f1e366efe695e1f11a38cb463efeaf))
* Bypass check_thresholds signal for sensors without thresholds ([4d8792a](https://github.com/arthurdedeus/lora-api/commit/4d8792a7566fd3b32b2a1beac823762cd0730089))
* Fix casefold usage to use title instead ([3b4ff9e](https://github.com/arthurdedeus/lora-api/commit/3b4ff9e6e9f8e56f12d16a2eb9432fb94d9de2c3))
* Fix Celery Regex implementation. ([0455501](https://github.com/arthurdedeus/lora-api/commit/04555015dd5106c0bf76611c3d0498e05ef7fc54))
* Fix celery terraform files. ([bde7ddd](https://github.com/arthurdedeus/lora-api/commit/bde7ddd63a3e418c80e374973ab0a6126704a338))
* Fix Django3 deprecations and migrations ([66f8eeb](https://github.com/arthurdedeus/lora-api/commit/66f8eebb109c0d246eeb894d46f0c581c8ac9bd3))
* Fix encoding keyword to support both python 2 and 3 ([1fa9f49](https://github.com/arthurdedeus/lora-api/commit/1fa9f496254b8f824503243705e15b8fdfcb0e33))
* Fix file deletion flow on setup.py. ([9003ba7](https://github.com/arthurdedeus/lora-api/commit/9003ba777a5038e11c03e152bf70d07173f8262c))
* Fix how the project name is filled throughout the files ([777b881](https://github.com/arthurdedeus/lora-api/commit/777b8819744315149b0b278b9969a892a24d9c9b))
* Fix join use. ([b99e36b](https://github.com/arthurdedeus/lora-api/commit/b99e36b62e0214dc10ce1ff6f8ef01e01c7605ae))
* Fix logic on file deletion. ([f05dc52](https://github.com/arthurdedeus/lora-api/commit/f05dc52fa84356543bcc66370cdc661cf64c8989))
* Fix missing backslash on circleci config ([e81879b](https://github.com/arthurdedeus/lora-api/commit/e81879be365eccef07bb7f351d1fc3ee02dabe21))
* Fix missing import path on sentry_sdk for DjangoIntegration ([22f19ba](https://github.com/arthurdedeus/lora-api/commit/22f19ba396464d371d0367d74638d1f93ab2ca8b))
* Fix missing name on circleci config file ([00d2411](https://github.com/arthurdedeus/lora-api/commit/00d24118cdbfbc02aabedff253fbe746f0948950))
* Fix not_celery tags persisting ([ce63e40](https://github.com/arthurdedeus/lora-api/commit/ce63e40eb2294d0737e60887be1f6d5881c925af))
* Fix not_celery usage ([ae5f427](https://github.com/arthurdedeus/lora-api/commit/ae5f4271fc324728401108038524ba8f8f6534b6))
* Fix password creation for Terraform. ([98483d0](https://github.com/arthurdedeus/lora-api/commit/98483d0005e22980d47e431e7e2d3cce79f07531))
* Fix placeholder tags in case of start of file. ([e657659](https://github.com/arthurdedeus/lora-api/commit/e657659a3d8187c11dac0b1578ff01a91b80e5a1))
* Fix README templating ([f27a379](https://github.com/arthurdedeus/lora-api/commit/f27a379738eb3835d9f54cdc5dadeaa4beb55401))
* Fix setup identation ([6af0f18](https://github.com/arthurdedeus/lora-api/commit/6af0f185d9a136860e65944167c10400e70dc436))
* Fix support for python < 3 ([0a13cb2](https://github.com/arthurdedeus/lora-api/commit/0a13cb21e6fe62239c30549926874c7794c92e21))
* Fix support to python2.7 ([6fbe036](https://github.com/arthurdedeus/lora-api/commit/6fbe0360ca1eb7d282fd7d71558794561de84e5e))
* Fix terminal usage on setup ([035891f](https://github.com/arthurdedeus/lora-api/commit/035891fcf54f8edddef235461a2060d209d1e0b7))
* Fix typo. ([a80a1eb](https://github.com/arthurdedeus/lora-api/commit/a80a1eb02ea0338f5c0f7e0bd94a7c804440067c))
* Fix usage of old raven_contrib SentryHandler ([f7e7a61](https://github.com/arthurdedeus/lora-api/commit/f7e7a615a6590be8f5398d3ab8c0264cc0650216))
* Force utf-8 encoding on files ([1137e06](https://github.com/arthurdedeus/lora-api/commit/1137e066155f9f3de3cae44bfc4efc59052f9c67))
* Import RE on setup. ([39ae9d1](https://github.com/arthurdedeus/lora-api/commit/39ae9d188bb7c6bc9d94fbcb28f1245c49fddc4f))
* Override TimestampModel save method ([2301969](https://github.com/arthurdedeus/lora-api/commit/2301969c16e0ed4fe86a210dcd4e47d3d36389b4))
* Remove old user related migrations ([e38f648](https://github.com/arthurdedeus/lora-api/commit/e38f6489cda8afbb37097dd492a2d4143a890a7b))
* Replace boilerplate with the project name ([f74198b](https://github.com/arthurdedeus/lora-api/commit/f74198b86e32f4d3a88264704f415d7bb91d5d59))
* **settings:** Add missing SITE_ID ([18be981](https://github.com/arthurdedeus/lora-api/commit/18be9818c633891c4e673cf498f71352b30e8d61))
* **setup:** Fix input not being str on iterm + zsh ([8adf4f0](https://github.com/arthurdedeus/lora-api/commit/8adf4f0eb0f64ab9e6ed05349b1fd7d470be33a0))
* update drf-yasg version ([f7aafa4](https://github.com/arthurdedeus/lora-api/commit/f7aafa444444da2b802d49361007ba6119266d71))
* Update initial accounts migration ([6ede23d](https://github.com/arthurdedeus/lora-api/commit/6ede23d0e066836863cf085f93268c14104e9f6b))
* Update support to python3 ([bc491a2](https://github.com/arthurdedeus/lora-api/commit/bc491a2a2f7ac24f94cc1c8d79ec19e23d47777c))


### Features

*  Add pull_request_template.md. ([5d84d80](https://github.com/arthurdedeus/lora-api/commit/5d84d8099c7499b487d675eee247c68ad63b190d))
* Add back Celery tags. ([89e2470](https://github.com/arthurdedeus/lora-api/commit/89e2470e8720fe2fcd5a86c73b52bc61fa82ce47))
* Add BaseUserAdmin ([d832374](https://github.com/arthurdedeus/lora-api/commit/d8323746bf6ac5e1b244caa4644dfe40f6d1521e))
* Add Celery setup to the boilerplate. ([56e12a7](https://github.com/arthurdedeus/lora-api/commit/56e12a775befc7b2eb5b477afe7a8dd59fa932e2))
* Add circleci config file ([d9d35d3](https://github.com/arthurdedeus/lora-api/commit/d9d35d3f6bd3d051c939b16c2143bb93860a0c3b))
* Add env.example conversion to .env on setup ([c501724](https://github.com/arthurdedeus/lora-api/commit/c501724b451e64038a5a57815e5dfd738edd0f01))
* Add local bucket creation ([cb2a51e](https://github.com/arthurdedeus/lora-api/commit/cb2a51e77d7c779a52f80eebd6640ae97ce54024))
* Add methods to return models' data ([f3b111a](https://github.com/arthurdedeus/lora-api/commit/f3b111a5cfad1fd8244913a10fdc29e45bb776fb))
* Add no_celery and update sentry settings ([1d2f78f](https://github.com/arthurdedeus/lora-api/commit/1d2f78f1f0f3432163e108ac8fe519879cfb206a))
* Add redis option to setup (true if celery or websockets) ([9226f31](https://github.com/arthurdedeus/lora-api/commit/9226f31aab9dc949027675985519bca217a76b15))
* Add Redis to boilerplate. ([a8b09d2](https://github.com/arthurdedeus/lora-api/commit/a8b09d2d4db6a80ba9fa2e73055894c2efb35159))
* Add sentry env ([1e46d43](https://github.com/arthurdedeus/lora-api/commit/1e46d43ae7704ddd2723fdb93d021e0f3e2a8322))
* Add Socials support for Regex implementation. ([33d945a](https://github.com/arthurdedeus/lora-api/commit/33d945af9f65fbba7f9577dc619bb1c5c5b6d200))
* Add swagger quickstart to boilerplate ([dcc75dd](https://github.com/arthurdedeus/lora-api/commit/dcc75dda2b392d9d27a2c01eadf44a97e00e02e5))
* add terraform integration ([8ce8ec5](https://github.com/arthurdedeus/lora-api/commit/8ce8ec5646a7b284ab8576f21058c9d1dc644e69))
* Add TimestampModel helper ([86eb77d](https://github.com/arthurdedeus/lora-api/commit/86eb77d738bbd0c9aa2af50891b467365ddcbfa5))
* Add WebSockets option ([b1245cd](https://github.com/arthurdedeus/lora-api/commit/b1245cd5ecc57eb8187f38d24662d058d9224506))
* **auth:** Add auth options on setup ([6d5715b](https://github.com/arthurdedeus/lora-api/commit/6d5715bca41598c0ee2ecefdd6da2a6617a2e8c1))
* **auth:** Add authentication system without social ([398c8b1](https://github.com/arthurdedeus/lora-api/commit/398c8b13c2c18c2e1170d5471411384c64b0b50f))
* **auth:** Add authentication system without social ([bb49f27](https://github.com/arthurdedeus/lora-api/commit/bb49f270573b20ce030e8476deb32eeab417eec2))
* **auth:** Add authentication system without social ([301d26f](https://github.com/arthurdedeus/lora-api/commit/301d26f5f11bf1fbff033f980f470522c02196b2))
* Bump Celery version ([cf7963f](https://github.com/arthurdedeus/lora-api/commit/cf7963f52b3bd4e9043e8c4c22411f3bc7163bec))
* Bump Django & supporting libs versions ([a7ffb82](https://github.com/arthurdedeus/lora-api/commit/a7ffb825a9480ef665a30d040687de52681de2ae))
* Create log and sensor models ([6b80006](https://github.com/arthurdedeus/lora-api/commit/6b8000698eaa8d3dffa5706844f20d1c8cf7accd))
* Create sensors module and fucas webhook ([a373a10](https://github.com/arthurdedeus/lora-api/commit/a373a10d3872bcf4c4f3be63e7e72a648081d600))
* Create SensorViewSet ([f06e113](https://github.com/arthurdedeus/lora-api/commit/f06e113078b0f9fdc1500c734bb85c287f35fbff))
* Create signal to check if log's measurements crossed thresholds and create warnings ([166366d](https://github.com/arthurdedeus/lora-api/commit/166366d3a20e93610a4109442ce6d1c0024fa4f7))
* Create warning model ([7eda9aa](https://github.com/arthurdedeus/lora-api/commit/7eda9aa024a149fcf5c42a184d6393e2ef2f3479))
* Create warning threshold model ([70d6291](https://github.com/arthurdedeus/lora-api/commit/70d6291a6237b6cada82e71c664cc9f7dbe95606))
* **database:** Add postgres database ([386061d](https://github.com/arthurdedeus/lora-api/commit/386061d5946cb08be37f1c0eca25f477a0969003))
* **guide:** Add initial setup guide ([f7b37be](https://github.com/arthurdedeus/lora-api/commit/f7b37be9b8606fdccaf13cd17fd720e2f63ac234))
* Implement log creation in webhook ([f6b1040](https://github.com/arthurdedeus/lora-api/commit/f6b1040b4ab4523d5f7a0c05f461bff16a8bcd7c))
* Install Redis and Celery for Terraform. ([1dc4cf6](https://github.com/arthurdedeus/lora-api/commit/1dc4cf6f4a3246b846b6bda3b73590351528b780))
* Set up signals settings ([28de81a](https://github.com/arthurdedeus/lora-api/commit/28de81acfe30a5f6c065817669bdb650cc2a4167))
* **setup:** Add docker ([45b471c](https://github.com/arthurdedeus/lora-api/commit/45b471ce722b6c4f81c35a9964690f5f152fb204))
* **setup:** Add gitignore file ([1efa0a8](https://github.com/arthurdedeus/lora-api/commit/1efa0a88c6eb51e4e951cc63f1ea1c883f5808ba))
* **setup:** Add README file ([2da82df](https://github.com/arthurdedeus/lora-api/commit/2da82df9d9dc6592350e1be7eed257b5e8c76043))
* **setup:** Start django app ([e51cf58](https://github.com/arthurdedeus/lora-api/commit/e51cf58100601df4c89865940cf0fa6681aa863f))
* **social:** Add base socialaccount structure ([a837e25](https://github.com/arthurdedeus/lora-api/commit/a837e254e767e5463f62bf0bf0c233911f5e1f7a))
* **social:** Add google + facebook providers ([62eb99b](https://github.com/arthurdedeus/lora-api/commit/62eb99b16322996245558cf47b07e2932e534a1f))
* **social:** Add social accounts to setup ([6c527cd](https://github.com/arthurdedeus/lora-api/commit/6c527cdf11692363b643d1a7c655919c2b6894a8))
* Update basic logging to include real IPs ([5545318](https://github.com/arthurdedeus/lora-api/commit/5545318398ff049669b34a5f5cc004340c6b7935))
* Update boilerplate settings ([41372c4](https://github.com/arthurdedeus/lora-api/commit/41372c41791b06eec7bce18a3e14d3f32ad8c8cb))
* Update env.example file ([2f8fccc](https://github.com/arthurdedeus/lora-api/commit/2f8fccccaebeb7afa39e0efe0502c46194886b3e))
* Update README ([cc66bc9](https://github.com/arthurdedeus/lora-api/commit/cc66bc9c07e1298b15b42faf55b116887b733827))
* Update requirements ([5504e6e](https://github.com/arthurdedeus/lora-api/commit/5504e6e937c93bd7e71695e854b87f8f6c1f5ff5))
* Update requirements ([22c23f5](https://github.com/arthurdedeus/lora-api/commit/22c23f500440f3052129652ed0172da8a753590c))
* Update setup file ([1583334](https://github.com/arthurdedeus/lora-api/commit/1583334ecb666bf8563c7ad840463ba8dd6242ce))
* Update storage settings ([2bf30a3](https://github.com/arthurdedeus/lora-api/commit/2bf30a3c262a38e0c6ed5a5826893c57a7c5d5e2))
* Update terraform files ([d8fedc8](https://github.com/arthurdedeus/lora-api/commit/d8fedc8fbd8108af4b0ae1699f9f40b508121b08))


