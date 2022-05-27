using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PacketManager : MonoSingleton<PacketManager>
{
    /// <summary>
    /// Called when parse is ended<br/>
    /// OnHandlePacket(type, (name of members, data of members));
    /// </summary>
    public event Action<string, (List<string>, List<string>)> OnHandlePacket;

    #region DEFINE

    const char TYPE        = '#';
    const char MEMBER      = '$';
    const char VALUE       = '=';
    const char ENDOFMEMBER = '&';
    const char TERMINATOR  = ';';

    #endregion

    Exception _invalidPacketException;

    private void Awake()
    {
        _invalidPacketException = new Exception("Packet is invalid");
    }


    /// <summary>
    /// Parses Packet
    /// </summary>
    /// <param name="data">response</param>
    public void ParsePacket(string data)
    {
        Debug.Log(data);

        string[] datas = data.Split(TERMINATOR);

        for (int i = 0; i < datas.Length - 1; ++i)
        {
            if (datas[i][0] == TYPE)
            {
                #region TYPE

                int typeEndIdx = datas[i].IndexOf(TYPE, 1);

                if (typeEndIdx <= 0) throw _invalidPacketException;

                string type = datas[i].Substring(1, typeEndIdx - 1);

                #endregion

                if (datas[i].Length <= typeEndIdx + 1)
                {
                    OnHandlePacket(type, (null, null));
                    return;
                } // For packet which only contains type.

                #region Member Group

                if (datas[i][typeEndIdx + 1] != MEMBER) throw _invalidPacketException;

                int memberStartIdx = typeEndIdx + 1;
                int memberEndIdx = datas[i].IndexOf(ENDOFMEMBER, memberStartIdx + 1);

                if (memberEndIdx <= memberStartIdx) throw _invalidPacketException;


                string member = datas[i].Substring(memberStartIdx + 1, memberEndIdx - memberStartIdx - 1);

                #endregion

                OnHandlePacket(type, ParseMember(member));
            }
            else
            {
                throw _invalidPacketException;
            }
        }
    }


    private (List<string>, List<string>) ParseMember(string data)
    {
        string[] members   = data.Split(MEMBER);
        string[] temp      = new string[2];
        List<string> name  = new List<string>();
        List<string> value = new List<string>();

        for (int i = 0; i < members.Length; ++i)
        {
            temp = members[i].Split(VALUE);
            name.Add(temp[0]);
            value.Add(temp[1]);
        }

        return (name, value);
    }

}
