# 使用 paramiko 库通过 SFTP 协议将文件从本地路径上传到远程服务器的指定路径
import paramiko


def sftp_transfer_file(local_file, remote_path,
                       hostname='10.192.110.211',
                       port=2222, username='db', password='123456'):
    """
    通过SFTP协议上传文件到远程服务器。

    :param local_path: 要上传的本地文件路径。
    :param remote_path: 服务器上的远程文件路径。
    :param hostname: 远程服务器的IP地址或主机名。
    :param port: SSH端口，默认为22。
    :param username: 登录远程服务器的用户名。
    :param password: 登录远程服务器的密码。
    """
    # 创建Transport对象并尝试连接
    transport = paramiko.Transport((hostname, port))
    try:
        transport.connect(username=username, password=password)
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials.")
        return False
    except paramiko.SSHException as sshException:
        print(f"Could not establish SSH connection: {sshException}")
        return False
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        return False

    # 创建SFTP客户端
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        # 上传文件
        remote_file = remote_path + '/' + local_file.split('/')[-1]
        sftp.put(local_file, remote_file)
        print(f"File '{local_file}' successfully uploaded to '{remote_file}'.")
    except IOError as e:
        print(f"File transfer failed: {e}")
        return False
    except paramiko.SFTPError as sftpError:
        print(f"SFTP error: {sftpError}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    finally:
        # 关闭SFTP客户端和Transport连接
        sftp.close()
        transport.close()
    return True


if __name__ == "__main__":
    # 使用示例
    # 请替换以下参数为你的服务器信息和文件路径
    local_file = 'D:/auto/AutoTest/Launcher_test/report.html'
    remote_path = '/home/report/AppTest/launcher'
    # 调用函数并传入参数
    upload_success = sftp_transfer_file(local_file=local_file, remote_path=remote_path)
    if upload_success:
        print("Transfer completed successfully.close")
    else:
        print("Transfer failed.")
