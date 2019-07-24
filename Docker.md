# コマンド一覧
| 実行内容          | コマンド                                             |
| ----------------- | ---------------------------------------------------- |
| コンテナ作成/実行 | docker container run Dockerイメージ名　実行コマンド  |
| バージョン確認    | docker version                                       |
| 実行環境確認      | docker system info                                   |
| ディスク利用状況  | docker system df -v                                  |
| イメージDL        | docker pull イメージ名                               |
| イメージ一覧      | docker image ls [オプション] [レポジトリ名]          |
| コンテナ状態確認  | docker container ps                                  |
| コンテナ詳細確認  | docker container stats -                             |
| コンテナ停止      | docker stop 名前                                     |
| イメージ取得      | docker image pull [オプション] イメージ名[:タグ名]   |
| イメージ詳細確認  | docker image inspect [イメージ名]                    |
| 検索              | docker search [オプション] 検索キーワード            |
| イメージ削除      | docker image rm [オプション] イメージ名 [イメージ名] |
| イメージ削除      | docker image prune [オプション]                      |
|                   | docker container pause                               |
|                   | docker nerwork ls                                    |