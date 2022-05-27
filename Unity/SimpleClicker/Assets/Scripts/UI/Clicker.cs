using System.IO;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Clicker : MonoBehaviour
{
   public int increaseAmount = 2;
   string uuid = "";

   private void Awake()
   {
      string path = Application.persistentDataPath + "/uuid";

      if (!File.Exists(path))
      {
         System.Guid guid = System.Guid.NewGuid();
         uuid = guid.ToString();
         File.WriteAllText(path, uuid);
      }
      else
      {
         uuid = File.ReadAllText(path);
      }

      Debug.Log(uuid);
   }

   public void IncreaseScore()
   {
      GameManager.Instance.Score += increaseAmount;
   }

   public void LoadScore()
   {
      StartCoroutine(RequestSender.Instance.GetScore(uuid, GameManager.Instance.Score));
   }

   public void SaveScore()
   {
      StartCoroutine(RequestSender.Instance.SaveScore(uuid, GameManager.Instance.Score));
   }

   public void LoadLeaderboard()
   {
      StartCoroutine(RequestSender.Instance.GetScore("", 10));
   }

   
   // private void OnApplicationQuit()
   // {
   //    SaveScore();
   // }
}
