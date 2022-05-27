using System.Text;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScoreHandler : MonoBehaviour
{
   public ScoreRenderer renderer;
   public UnityEngine.UI.Text leaderBoard;

   private void Start()
   {
      PacketHandler.Instance.AddHandler("MYSCORE", members => {
         GameManager.Instance.Score = System.Int32.Parse(members.Item2[1]);
         renderer.UpdateText();
      });

      PacketHandler.Instance.AddHandler("SCOREDATA", members => {
         StringBuilder sb = new StringBuilder();

         for (int i = 1; i < members.Item2.Count; i += 2)
         {
            sb.Append($"{i + 1}. 익명의 누군가: {members.Item2[i]}\r\n");
         }

         leaderBoard.text = sb.ToString();
      });
   }
}
