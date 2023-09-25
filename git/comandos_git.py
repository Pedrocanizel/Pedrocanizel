# GIT-CHEATSEET  https://ndpsoftware.com/git-cheatsheet.html#loc=workspace;

# GERAÇÃO DE CHAVES SSH
# ssh-keygen -t ed25519 -C "email@dominio" (gera uma chave ssh)
# ssh -T git@github (testa a conexão com o github)

# GIT CONFIG
# git config --global user.name "Nome"
# git config --global user.email "Email"

# GIT INIT
# git init <nome-do-repositorio>

# GIT ADD
# git add <nome-do-arquivo>
# git add . (adiciona todos os arquivos)
# git add -u (adiciona todos os arquivos modificados)

# GIT STATUS
# git status (mostra o status do repositório)

# GIT COMMIT
# git commit -m "mensagem" (cria um commit com a mensagem)
# git commit -am "mensagem" (cria um commit com a mensagem e adiciona todos os arquivos modificados)
# git commit --amend -m "mensagem" (altera a mensagem do último commit)
# git commit --amend --no-edit (altera o último commit sem alterar a mensagem)
# git commit -v (mostra as alterações feitas no commit)
# git commit -v -m "mensagem" (mostra as alterações feitas no commit e cria um commit com a mensagem)

# GIT BRANCH
# git branch (lista as branchs)
# git branch <nome-da-branch> (cria uma branch)
# git branch -d <nome-da-branch> (deleta uma branch)

# GIT CHECKOUT
# git checkout <nome-da-branch> (altera para a branch informada)
# git checkout -b <nome-da-branch> (cria uma branch e altera para ela)

# GIT LS-TREE e GIT SHOW
# git ls-tree <nome-da-branch> (mostra os arquivos do último commit)
# git show <nome-da-branch> (mostra as alterações da branch)
# git show <hash-do-commit> (mostra as alterações do commit)

# GIT MERGE
# git merge <nome-da-branch> (faz o merge da branch informada com a branch atual)

# GIT DIFF
# git diff (mostra as alterações feitas nos arquivos)
# git diff --name-only (mostra apenas os nomes dos arquivos modificados)
# git diff --name-status (mostra os nomes dos arquivos modificados e o tipo de modificação)
# git diff --cached (mostra as diferenças entre a versão atual dos arquivos e a versão indexada (stage))
# git diff <nome-do-arquivo> (mostra as alterações feitas no arquivo)

# HEAD
# HEAD é um ponteiro que aponta para o último commit da branch atual

# GIT-REMOTE
# git remote add origin <url-do-repositorio> (adiciona o repositório remoto)
# git remote -v (mostra os repositórios remotos)
# git remote set-url origin <url-do-repositorio> (altera a url do repositório remoto)
# git remote rm origin (remove o repositório remoto)

# GIT-PUSH
# git push origin <nome-da-branch> (envia os commits para o repositório remoto)
# git push origin <nome-da-branch> --force (envia os commits para o repositório remoto forçando o push)
# git push origin --delete <nome-da-branch> (deleta a branch remota)
# git push --set-upstream origin <nome-da-branch> (estabelece a ligação entre a branch local e a branch remota, permitindo que as futuras atualizações sejam feitas com apenas o comando git push)

# GIT-PULL
# git pull origin <nome-da-branch> (atualiza o repositório local com as alterações do repositório remoto)

# GIT-CLONE
# git clone <url-do-repositorio> (clona o repositório remoto para o repositório local)
# git clone -b <minha-branch> <url-do-repositorio> (clona o repositório remoto para o repositório local com a branch informada)
# git clone --recursive <url-do-repositorio> (clona o repositório remoto para o repositório local com os submódulos)

# GIT-FETCH
# git fetch origin <nome-da-branch> (atualiza o repositório local com as alterações do repositório remoto)
# git fetch origin --prune (remove as branchs remotas que não existem mais no repositório remoto)

# GIT-REVERT e GIT RESET
# git revert <hash-do-commit> (cria um novo commit com as alterações do commit informado)
# git reset --soft <hash-do-commit> (remove o commit informado e mantém as alterações nos arquivos)
# git reset --mixed <hash-do-commit> (remove o commit informado e mantém as alterações nos arquivos, porém, as alterações são removidas do stage)
# git reset --hard <hash-do-commit> (remove o commit informado e as alterações nos arquivos)

