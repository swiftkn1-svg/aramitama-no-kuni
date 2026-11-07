#!/usr/bin/env bash
# ==============================================================================
# 『荒魂の國 - 乱世漂泊録 -』 GitHub 初期リポジトリ セットアップ＆Pushスクリプト
# ==============================================================================
set -e

REPO_URL=${1:-""}

echo "⛩️ 『荒魂の國 - 乱世漂泊録 -』 Git初期化を開始します..."

if [ ! -d ".git" ]; then
    git init
    git branch -M main
fi

git add .
git commit -m "feat: initial commit of Aramitama-no-Kuni (MASTER VISION v2.2, Izumo 5 Acts, Historical Research & Core Data)" || true

if [ -n "$REPO_URL" ]; then
    if git remote | grep -q "^origin$"; then
        git remote set-url origin "$REPO_URL"
    else
        git remote add origin "$REPO_URL"
    fi
    echo "🚀 リモートリポジトリ ($REPO_URL) へ Push しています..."
    git push -u origin main
    echo "✅ Push が完了しました！"
else
    echo "ℹ️ ローカルコミットが完了しました！"
    echo "   GitHubへPushする場合は以下のように実行してください："
    echo "   ./init_and_push.sh https://github.com/<あなたのユーザー名>/aramitama-no-kuni.git"
    echo "   （または gh repo create aramitama-no-kuni --private --source=. --remote=origin --push）"
fi
